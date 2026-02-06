#!/usr/bin/env python3
"""
Automated File Management System
A production-ready file organization tool with logging, scheduling, and advanced features.

Author: Eric Jang
GitHub: https://github.com/EricJang-sud/Eric-Jang-Data-Portfolio
License: MIT
"""

# ============================================================================
# CONFIGURATION - CUSTOMIZE THESE VARIABLES
# ============================================================================

# Target folder path (leave empty "" to be prompted)
FOLDER_PATH = r"" 

# Size thresholds in bytes (customize as needed)
SIZE_THRESHOLD_MB = 1 * 1024 * 1024      # 1 MB
SIZE_THRESHOLD_GB = 1 * 1024 * 1024 * 1024  # 1 GB

# Folder names for organized files
FOLDER_LARGE = "above 1GB"
FOLDER_MEDIUM = "1MB-1GB"

# Logging configuration
ENABLE_LOGGING = True
LOG_FILE = "file_manager.log"
LOG_LEVEL = "INFO"  # Options: DEBUG, INFO, WARNING, ERROR

# Advanced options
RECURSIVE_SCAN = True  # Scan subdirectories
EXCLUDE_HIDDEN = True  # Skip hidden files (starting with .)
BACKUP_BEFORE_MOVE = False  # Create backup of file locations

# File type filters (leave empty to process all files)
# Example: ['.pdf', '.docx', '.mp4'] or [] for all files
ALLOWED_EXTENSIONS = []

# Exclude specific folders from scanning
EXCLUDED_FOLDERS = ['.git', 'node_modules', '__pycache__', '.vscode']

# ============================================================================
# DO NOT EDIT BELOW THIS LINE
# ============================================================================

import os
import sys
import json
import shutil
import logging
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from datetime import datetime
from collections import defaultdict


class FileManagerLogger:
    """Handles logging configuration and operations."""
    
    def __init__(self, log_file: str = LOG_FILE, level: str = LOG_LEVEL):
        """Initialize logger with file and console handlers."""
        self.logger = logging.getLogger('FileManager')
        self.logger.setLevel(getattr(logging, level.upper()))
        
        # Prevent duplicate handlers
        if self.logger.handlers:
            self.logger.handlers.clear()
        
        # File handler
        if ENABLE_LOGGING:
            fh = logging.FileHandler(log_file, encoding='utf-8')
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(logging.Formatter(
                '%(asctime)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            ))
            self.logger.addHandler(fh)
        
        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(logging.Formatter('%(message)s'))
        self.logger.addHandler(ch)
    
    def get_logger(self):
        """Return configured logger instance."""
        return self.logger


class FileOrganizer:
    """Main class for file organization with advanced features."""
    
    def __init__(self, source_directory: str):
        """
        Initialize the FileOrganizer.
        
        Args:
            source_directory: Path to the directory containing files to organize
        """
        self.source_dir = Path(source_directory).resolve()
        self.logger = FileManagerLogger().get_logger()
        
        # Statistics tracking
        self.stats = {
            'scanned': 0,
            'large': 0,
            'medium': 0,
            'small': 0,
            'errors': 0,
            'skipped': 0
        }
        
        # File type distribution
        self.file_types = defaultdict(int)
        
        # Validate source directory
        self._validate_directory()
        
        self.logger.info(f"Initialized FileOrganizer for: {self.source_dir}")
    
    def _validate_directory(self):
        """Validate that source directory exists and is accessible."""
        if not self.source_dir.exists():
            raise ValueError(f"Source directory does not exist: {self.source_dir}")
        if not self.source_dir.is_dir():
            raise ValueError(f"Source path is not a directory: {self.source_dir}")
        
        # Check read/write permissions
        if not os.access(self.source_dir, os.R_OK | os.W_OK):
            raise PermissionError(f"Insufficient permissions for: {self.source_dir}")
    
    def get_file_category(self, file_size: int) -> str:
        """
        Categorize file based on size thresholds.
        
        Args:
            file_size: Size of file in bytes
            
        Returns:
            Category string: 'large', 'medium', or 'small'
        """
        if file_size >= SIZE_THRESHOLD_GB:
            return 'large'
        elif file_size >= SIZE_THRESHOLD_MB:
            return 'medium'
        else:
            return 'small'
    
    def format_size(self, size_bytes: int) -> str:
        """Convert bytes to human-readable format."""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} PB"
    
    def should_process_file(self, file_path: Path) -> bool:
        """
        Determine if file should be processed based on filters.
        
        Args:
            file_path: Path to the file
            
        Returns:
            True if file should be processed, False otherwise
        """
        # Skip hidden files if configured
        if EXCLUDE_HIDDEN and file_path.name.startswith('.'):
            self.logger.debug(f"Skipping hidden file: {file_path.name}")
            return False
        
        # Check file extension filter
        if ALLOWED_EXTENSIONS and file_path.suffix.lower() not in ALLOWED_EXTENSIONS:
            self.logger.debug(f"Skipping file (extension filter): {file_path.name}")
            return False
        
        # Skip files in excluded folders
        for excluded in EXCLUDED_FOLDERS:
            if excluded in file_path.parts:
                self.logger.debug(f"Skipping file in excluded folder: {file_path}")
                return False
        
        # Skip files already in target folders
        if FOLDER_LARGE in file_path.parts or FOLDER_MEDIUM in file_path.parts:
            return False
        
        return True
    
    def scan_files(self) -> Dict[str, List[Tuple[Path, int]]]:
        """
        Scan directory and categorize files by size.
        
        Returns:
            Dictionary with categories and file lists
        """
        categorized = {'large': [], 'medium': [], 'small': []}
        
        self.logger.info(f"Scanning directory: {self.source_dir}")
        print("=" * 70)
        
        # Choose scan method based on RECURSIVE_SCAN setting
        scan_method = self.source_dir.rglob('*') if RECURSIVE_SCAN else self.source_dir.glob('*')
        
        for item in scan_method:
            if item.is_dir():
                continue
            
            if not self.should_process_file(item):
                self.stats['skipped'] += 1
                continue
            
            try:
                file_size = item.stat().st_size
                category = self.get_file_category(file_size)
                categorized[category].append((item, file_size))
                
                # Track file type distribution
                self.file_types[item.suffix.lower() or 'no_extension'] += 1
                self.stats['scanned'] += 1
                
            except (OSError, PermissionError) as e:
                self.logger.warning(f"Could not access {item.name}: {e}")
                self.stats['errors'] += 1
        
        return categorized
    
    def create_backup_manifest(self, categorized_files: Dict[str, List[Tuple[Path, int]]]) -> str:
        """
        Create a backup JSON file with original file locations.
        
        Args:
            categorized_files: Dictionary of categorized files
            
        Returns:
            Path to backup manifest file
        """
        manifest = {
            'timestamp': datetime.now().isoformat(),
            'source_directory': str(self.source_dir),
            'files': []
        }
        
        for category, files in categorized_files.items():
            if category == 'small':
                continue
            for file_path, file_size in files:
                manifest['files'].append({
                    'original_path': str(file_path),
                    'filename': file_path.name,
                    'size': file_size,
                    'category': category
                })
        
        backup_file = self.source_dir / f"backup_manifest_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(backup_file, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2)
        
        self.logger.info(f"Backup manifest created: {backup_file}")
        return str(backup_file)
    
    def organize_files(self, dry_run: bool = False) -> Dict[str, int]:
        """
        Organize files into folders based on size.
        
        Args:
            dry_run: If True, simulate without moving files
            
        Returns:
            Statistics dictionary
        """
        start_time = datetime.now()
        categorized_files = self.scan_files()
        
        # Print summary
        print(f"\n📊 Scan Summary:")
        print(f"   Files scanned: {self.stats['scanned']}")
        print(f"   Large files (≥ {self.format_size(SIZE_THRESHOLD_GB)}): {len(categorized_files['large'])}")
        print(f"   Medium files ({self.format_size(SIZE_THRESHOLD_MB)}-{self.format_size(SIZE_THRESHOLD_GB)}): {len(categorized_files['medium'])}")
        print(f"   Small files (< {self.format_size(SIZE_THRESHOLD_MB)}): {len(categorized_files['small'])} - will remain in place")
        print(f"   Skipped: {self.stats['skipped']}")
        
        if dry_run:
            print(f"\n🔍 DRY RUN MODE - No files will be moved")
            self.logger.info("Running in DRY RUN mode")
        
        # Create backup manifest if enabled
        if BACKUP_BEFORE_MOVE and not dry_run:
            backup_file = self.create_backup_manifest(categorized_files)
            print(f"\n💾 Backup manifest created: {backup_file}")
        
        # Create organization folders
        folder_paths = {}
        if not dry_run:
            for category, folder_name in [('large', FOLDER_LARGE), ('medium', FOLDER_MEDIUM)]:
                folder_path = self.source_dir / folder_name
                folder_path.mkdir(exist_ok=True)
                folder_paths[category] = folder_path
                self.logger.debug(f"Created folder: {folder_path}")
        
        print(f"\n{'🔍 Simulating' if dry_run else '📦 Organizing'} files...")
        print("=" * 70)
        
        # Process files
        for category in ['large', 'medium']:
            files = categorized_files[category]
            if not files:
                continue
            
            folder_name = FOLDER_LARGE if category == 'large' else FOLDER_MEDIUM
            print(f"\n📁 {folder_name}:")
            
            for file_path, file_size in files:
                try:
                    if not dry_run:
                        destination = folder_paths[category] / file_path.name
                        
                        # Handle name conflicts
                        counter = 1
                        while destination.exists():
                            stem = file_path.stem
                            suffix = file_path.suffix
                            destination = folder_paths[category] / f"{stem}_{counter}{suffix}"
                            counter += 1
                        
                        shutil.move(str(file_path), str(destination))
                        self.logger.info(f"Moved: {file_path.name} -> {folder_name}")
                    
                    print(f"   ✓ {file_path.name} ({self.format_size(file_size)})")
                    self.stats[category] += 1
                    
                except Exception as e:
                    self.logger.error(f"Error moving {file_path.name}: {e}")
                    print(f"   ✗ Error moving {file_path.name}: {e}")
                    self.stats['errors'] += 1
        
        # Calculate execution time
        execution_time = (datetime.now() - start_time).total_seconds()
        self.stats['execution_time'] = execution_time
        
        return self.stats
    
    def print_summary(self, dry_run: bool = False):
        """Print final summary with statistics."""
        print("\n" + "=" * 70)
        print(f"✅ {'Simulation' if dry_run else 'Organization'} Complete!")
        print("=" * 70)
        
        print(f"\n📈 Statistics:")
        print(f"   Files scanned: {self.stats['scanned']}")
        if self.stats['large'] > 0:
            print(f"   Large files moved: {self.stats['large']}")
        if self.stats['medium'] > 0:
            print(f"   Medium files moved: {self.stats['medium']}")
        if self.stats['skipped'] > 0:
            print(f"   Files skipped: {self.stats['skipped']}")
        if self.stats['errors'] > 0:
            print(f"   ⚠️  Errors: {self.stats['errors']}")
        
        total_moved = self.stats['large'] + self.stats['medium']
        print(f"\n   Total files {'that would be' if dry_run else ''} moved: {total_moved}")
        print(f"   Execution time: {self.stats.get('execution_time', 0):.2f} seconds")
        
        # File type distribution
        if self.file_types:
            print(f"\n📊 File Type Distribution:")
            sorted_types = sorted(self.file_types.items(), key=lambda x: x[1], reverse=True)
            for ext, count in sorted_types[:10]:  # Show top 10
                print(f"   {ext if ext != 'no_extension' else '(no extension)'}: {count}")
        
        print(f"\n💡 Note: Files smaller than {self.format_size(SIZE_THRESHOLD_MB)} were left in their original location")
        
        if ENABLE_LOGGING:
            print(f"📝 Detailed log saved to: {LOG_FILE}")


def main():
    """Main entry point with CLI argument parsing."""
    parser = argparse.ArgumentParser(
        description='Advanced File Management System - Organize files by size with logging and analytics',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage with configured path
  python file_manager_pro.py
  
  # Specify directory
  python file_manager_pro.py /path/to/files
  
  # Dry run to preview changes
  python file_manager_pro.py --dry-run
  
  # Show configuration
  python file_manager_pro.py --show-config
  
  # Generate statistics only
  python file_manager_pro.py --stats-only

Configuration:
  Edit the CONFIGURATION section at the top of this file to customize:
  - Folder paths and size thresholds
  - Logging preferences
  - File type filters and exclusions
  - Advanced options
        """
    )
    
    parser.add_argument(
        'directory',
        nargs='?',
        help='Directory to organize (overrides FOLDER_PATH config)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Simulate organization without moving files'
    )
    
    parser.add_argument(
        '--show-config',
        action='store_true',
        help='Display current configuration and exit'
    )
    
    parser.add_argument(
        '--stats-only',
        action='store_true',
        help='Show statistics without organizing files'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='File Manager Pro v2.0'
    )
    
    args = parser.parse_args()
    
    # Show configuration if requested
    if args.show_config:
        print("=" * 70)
        print("CURRENT CONFIGURATION")
        print("=" * 70)
        print(f"Folder Path: {FOLDER_PATH or '(Not set - will prompt)'}")
        print(f"Size Threshold (MB): {SIZE_THRESHOLD_MB / (1024*1024):.1f} MB")
        print(f"Size Threshold (GB): {SIZE_THRESHOLD_GB / (1024*1024*1024):.1f} GB")
        print(f"Logging Enabled: {ENABLE_LOGGING}")
        print(f"Log File: {LOG_FILE}")
        print(f"Recursive Scan: {RECURSIVE_SCAN}")
        print(f"Exclude Hidden: {EXCLUDE_HIDDEN}")
        print(f"Backup Before Move: {BACKUP_BEFORE_MOVE}")
        print(f"Allowed Extensions: {ALLOWED_EXTENSIONS or 'All files'}")
        print(f"Excluded Folders: {EXCLUDED_FOLDERS}")
        return 0
    
    # Determine directory
    directory = args.directory
    
    if not directory:
        if FOLDER_PATH and FOLDER_PATH.strip():
            directory = FOLDER_PATH.strip()
            print(f"Using configured folder path: {directory}")
        else:
            print("=" * 70)
            print("AUTOMATED FILE MANAGEMENT SYSTEM")
            print("=" * 70)
            print("\nThis system organizes files by size with:")
            print("  • Advanced logging and error handling")
            print("  • File type analytics")
            print("  • Backup manifests (optional)")
            print("  • Customizable filters and exclusions")
            print("\n" + "=" * 70)
            
            directory = input("\nEnter folder path to organize: ").strip()
            
            if not directory:
                print("❌ Error: No directory path provided")
                return 1
    
    # Clean up path
    directory = directory.strip('"').strip("'")
    directory = os.path.expanduser(directory)
    
    try:
        # Initialize organizer
        organizer = FileOrganizer(directory)
        
        # Stats only mode
        if args.stats_only:
            categorized = organizer.scan_files()
            print("\n📊 Statistics Summary:")
            print(f"   Total files scanned: {organizer.stats['scanned']}")
            print(f"   Large files: {len(categorized['large'])}")
            print(f"   Medium files: {len(categorized['medium'])}")
            print(f"   Small files: {len(categorized['small'])}")
            
            if organizer.file_types:
                print(f"\n📊 File Type Distribution:")
                sorted_types = sorted(organizer.file_types.items(), key=lambda x: x[1], reverse=True)
                for ext, count in sorted_types[:15]:
                    print(f"   {ext if ext != 'no_extension' else '(no extension)'}: {count}")
            return 0
        
        # Organize files
        stats = organizer.organize_files(dry_run=args.dry_run)
        
        # Print summary
        organizer.print_summary(dry_run=args.dry_run)
        
        return 0
        
    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
        return 1
    except PermissionError as e:
        print(f"❌ Permission Error: {e}")
        return 1
    except KeyboardInterrupt:
        print("\n\n⚠️  Operation cancelled by user")
        return 1
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        logging.exception("Unexpected error occurred")
        return 1


if __name__ == "__main__":
    sys.exit(main())
