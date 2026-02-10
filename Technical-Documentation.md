# Automated File Management System by Size - Technical Documentation

## Quick Start

### Prerequisites

- Python 3.6 or higher
- Command-line access (Terminal/CMD/PowerShell)

> **Note:** This tool can organize **any folder** on your system. The examples use Downloads folder for demonstration purposes, but you can use it for Documents, Desktop, project folders, backup directories, or any location you choose.

### Installation Options

#### Option A: Clone Repository (Recommended for Development)

**1. Clone the repository:**

> **Note:** The path below is an example. You can clone to **any location** on your system.

```bash
# Example: Clone to a specific location
git clone https://github.com/yourusername/file-management-system.git
cd file-management-system

# You can also clone to a custom location:
# git clone https://github.com/yourusername/file-management-system.git D:\MyProjects\file-manager
# git clone https://github.com/yourusername/file-management-system.git ~/projects/file-manager
```

**2. Configure and run** (see Configuration section below)

#### Option B: Download Single File (Portable Setup)

**1. Download the script:**
- Click on [`file_manager_pro.py`](file_manager_pro.py) in this repository
- Click "Raw" button
- Save the file to any location on your computer

**2. Save to your preferred location:**

> **Note:** These are examples only. Save the script to **any drive, folder, or location** you prefer.

- **Windows Examples:** 
  - `D:\Scripts\file_manager_pro.py`
  - `C:\Tools\file_manager_pro.py`
  - `E:\My Programs\Automation\file_manager_pro.py`

- **Mac/Linux Examples:** 
  - `~/scripts/file_manager_pro.py`
  - `/usr/local/bin/file_manager_pro.py`
  - `/Volumes/ExternalDrive/tools/file_manager_pro.py`

**3. Configure and run** (see Configuration section below)

### Configuration

**1. Open `file_manager_pro.py` in any text editor**

**2. Find the configuration section (around line 15) and set your target folder:**

```python
FOLDER_PATH = "/path/to/folder/you/want/to/organize"
```

**Path Examples (can be ANY folder on your system):**

> **Important:** All paths below are examples only. Replace with the actual folder you want to organize.

| Location Type | Windows Example | Mac/Linux Example |
|--------------|-----------------|-------------------|
| Downloads (demo) | `r"C:\Users\YourName\Downloads"` | `"/Users/YourName/Downloads"` |
| Documents | `r"C:\Users\YourName\Documents"` | `"/Users/YourName/Documents"` |
| Desktop | `r"C:\Users\YourName\Desktop"` | `"/Users/YourName/Desktop"` |
| Custom folder | `r"D:\MyFiles\Archives"` | `"/home/yourname/archives"` |
| Project folder | `r"C:\Projects\DataSets"` | `"/Users/YourName/projects/datasets"` |
| External drive | `r"E:\Backup"` | `"/Volumes/Backup"` |
| Network drive | `r"Z:\SharedFiles"` | `"/mnt/network/shared"` |

> **Remember:** Replace `YourName` and folder paths with your actual username and desired locations.

> **Important:** 
> - Windows: Use `r"` before the path and backslashes `\`
> - Mac/Linux: Use forward slashes `/`
> - The script location and target folder can be on different drives

**3. Save the file**

### Running the Script

**Navigate to where you saved the script:**

> **Note:** The paths below are examples only. Replace with your actual location - the script can be saved and run from **any drive or folder** on your system.

**Windows:**
```cmd
# Example if saved to D:\Scripts\ (replace with your actual path)
D:
cd Scripts

# Or use full path from anywhere (works regardless of current directory)
python "D:\Scripts\file_manager_pro.py" --dry-run

# Examples for other locations:
python "C:\MyFolder\file_manager_pro.py" --dry-run
python "E:\Tools\Python Scripts\file_manager_pro.py" --dry-run
```

**Mac/Linux:**
```bash
# Example if saved to ~/scripts/ (replace with your actual path)
cd ~/scripts

# Or use full path from anywhere (works regardless of current directory)
python ~/scripts/file_manager_pro.py --dry-run

# Examples for other locations:
python /usr/local/bin/file_manager_pro.py --dry-run
python /Volumes/ExternalDrive/tools/file_manager_pro.py --dry-run
```

**Run commands:**
```bash
# Preview changes (recommended first run)
python file_manager_pro.py --dry-run

# Organize files
python file_manager_pro.py
```

## Usage

### Basic Commands

> **Note:** Replace `/path/to/folder` with any actual folder you want to organize.

```bash
# Show current configuration
python file_manager_pro.py --show-config

# Preview without moving files
python file_manager_pro.py --dry-run

# Show statistics only
python file_manager_pro.py --stats-only

# Organize files (uses FOLDER_PATH from config)
python file_manager_pro.py

# Organize specific directory (overrides config - works with any path)
python file_manager_pro.py /path/to/folder
python file_manager_pro.py "C:\Users\Name\Documents"  # Windows example
python file_manager_pro.py ~/Desktop                   # Mac/Linux example
```

### Complete Setup Tutorial (Portable Installation)

This tutorial shows how to set up the script in a custom location and organize any folder.

#### Step 1: Download and Save

> **Note:** The paths shown are examples. Choose **any location** that works for you.

**Windows:**
1. Download `file_manager_pro.py` 
2. Save to your chosen location, for example:
   - `D:\Scripts\file_manager_pro.py`
   - `C:\MyTools\file_manager_pro.py`
   - `E:\Python Projects\file_manager_pro.py`

**Mac/Linux:**
1. Download `file_manager_pro.py`
2. Save to your chosen location, for example:
   - `~/scripts/file_manager_pro.py`
   - `/usr/local/bin/file_manager_pro.py`
   - `/opt/tools/file_manager_pro.py`

#### Step 2: Configure Target Folder

Open `file_manager_pro.py` in any text editor and modify line 15:

> **Important:** These are just examples. Set `FOLDER_PATH` to **any folder** you want to organize.

```python
# Example 1: Organize your Documents folder
FOLDER_PATH = r"C:\Users\John\Documents"  # Windows
FOLDER_PATH = "/Users/John/Documents"     # Mac/Linux

# Example 2: Organize a project folder on a different drive
FOLDER_PATH = r"D:\Projects\DataFiles"    # Windows
FOLDER_PATH = "/home/john/projects/data"  # Mac/Linux

# Example 3: Organize an external drive
FOLDER_PATH = r"E:\Backup\Photos"         # Windows
FOLDER_PATH = "/Volumes/Backup/Photos"    # Mac/Linux

# Example 4: Organize Downloads (commonly used, but optional)
FOLDER_PATH = r"C:\Users\John\Downloads"  # Windows
FOLDER_PATH = "/Users/John/Downloads"     # Mac/Linux
```

> **Key Point:** The script location (e.g., `D:\Scripts\`) and target folder (e.g., `C:\Users\John\Documents`) can be completely different locations on different drives!

#### Step 3: Run from Command Line

> **Note:** All paths below are examples. Replace with where you actually saved the script.

**Windows (examples assume script saved to D:\Scripts\):**
```cmd
# Method 1: Navigate to script location (example path - use your actual path)
D:
cd Scripts
python file_manager_pro.py --dry-run

# Method 2: Run from anywhere using full path (works from any directory)
python "D:\Scripts\file_manager_pro.py" --dry-run

# More examples from different locations:
python "C:\Tools\file_manager_pro.py" --dry-run
python "E:\My Programs\file_manager_pro.py" --dry-run

# Once satisfied with preview, run for real
python "D:\Scripts\file_manager_pro.py"
```

**Mac/Linux (examples assume script saved to ~/scripts/):**
```bash
# Method 1: Navigate to script location (example path - use your actual path)
cd ~/scripts
python file_manager_pro.py --dry-run

# Method 2: Run from anywhere using full path (works from any directory)
python ~/scripts/file_manager_pro.py --dry-run

# More examples from different locations:
python /usr/local/bin/file_manager_pro.py --dry-run
python /opt/tools/file_manager_pro.py --dry-run

# Once satisfied with preview, run for real
python ~/scripts/file_manager_pro.py
```

#### Step 4: Verify Results

After running, check your target folder to see the organization.

> **Example:** If you organized `/Users/John/Documents` (replace with your actual target folder):

**Before organizing `/Users/John/Documents`:**
```
Documents/
├── large_video.mp4 (2.5 GB)
├── presentation.pptx (25 MB)
├── notes.txt (5 KB)
└── report.pdf (10 MB)
```

**After organizing:**
```
Documents/
├── above 1GB/
│   └── large_video.mp4 (2.5 GB)
├── 1MB-1GB/
│   ├── presentation.pptx (25 MB)
│   └── report.pdf (10 MB)
└── notes.txt (5 KB)  ← Stayed in place (< 1MB)
```

The same organization structure applies to **any folder** you choose to organize.

### Windows-Specific Examples

> **Note:** Paths shown are examples. Replace with your actual script location and target folders.

```cmd
# Navigate to where you saved/cloned (example locations)
cd C:\path\to\file-management-system
cd D:\MyProjects\file-manager
cd E:\Tools\automation-scripts

# Run with any Windows path (examples - use your actual folders)
python file_manager_pro.py "C:\Users\YourName\Downloads"
python file_manager_pro.py "D:\Projects\DataFiles"
python file_manager_pro.py "E:\Backup"
python file_manager_pro.py "C:\Users\YourName\Desktop\Work Files"
```

### Mac/Linux-Specific Examples

> **Note:** Paths shown are examples. Replace with your actual script location and target folders.

```bash
# Navigate to where you saved/cloned (example locations)
cd /path/to/file-management-system
cd ~/projects/file-manager
cd /opt/tools/automation

# Run with any Unix path (examples - use your actual folders)
python file_manager_pro.py ~/Downloads
python file_manager_pro.py ~/Documents
python file_manager_pro.py /Volumes/ExternalDrive
python file_manager_pro.py ~/Desktop/ProjectFiles

# Make executable (optional)
chmod +x file_manager_pro.py
./file_manager_pro.py --dry-run
```

## Example Output

Here's what you'll see when running the script:

> **Note:** This example shows organizing a Downloads folder, but the output is identical for **any folder** you choose to organize (Documents, Desktop, project folders, etc.).

```
======================================================================
Scanning directory: /Users/john/Downloads
======================================================================

📊 Scan Summary:
   Files scanned: 247
   Large files (≥ 1.00 GB): 5
   Medium files (1.00 MB-1.00 GB): 42
   Small files (< 1.00 MB): 200 - will remain in place
   Skipped: 0

📦 Organizing files...
======================================================================

📁 above 1GB:
   ✓ ubuntu-22.04.iso (3.42 GB)
   ✓ movie.mkv (1.89 GB)
   ✓ backup.tar.gz (2.15 GB)

📁 1MB-1GB:
   ✓ presentation.pptx (12.45 MB)
   ✓ video.mp4 (234.67 MB)
   ... (40 more files)

======================================================================
✅ Organization Complete!
======================================================================

📈 Statistics:
   Files scanned: 247
   Large files moved: 5
   Medium files moved: 42
   
   Total files moved: 47
   Execution time: 2.34 seconds

📊 File Type Distribution:
   .mp4: 15
   .pdf: 12
   .jpg: 8

📝 Detailed log saved to: file_manager.log
```

> **Note:** The log file is saved in the same directory as the script, not in the target folder being organized.

## Configuration

All configuration options are at the top of `file_manager_pro.py`:

> **Note:** All path examples below can be replaced with **any folder** on your system.

```python
# Target folder path (examples - replace with your actual folder)
FOLDER_PATH = ""                           # Leave empty to be prompted
FOLDER_PATH = r"C:\Users\Name\Downloads"   # Windows example
FOLDER_PATH = "/Users/Name/Documents"      # Mac/Linux example

# Size thresholds (customize as needed)
SIZE_THRESHOLD_MB = 1 * 1024 * 1024      # 1 MB
SIZE_THRESHOLD_GB = 1 * 1024 * 1024 * 1024  # 1 GB

# Folder names for organized files
FOLDER_LARGE = "above 1GB"
FOLDER_MEDIUM = "1MB-1GB"

# Logging
ENABLE_LOGGING = True
LOG_FILE = "file_manager.log"
LOG_LEVEL = "INFO"

# Advanced options
RECURSIVE_SCAN = True              # Scan subdirectories
EXCLUDE_HIDDEN = True              # Skip hidden files
BACKUP_BEFORE_MOVE = False         # Create backup manifest
ALLOWED_EXTENSIONS = []            # Empty = all files
EXCLUDED_FOLDERS = ['.git', 'node_modules']
```

## Platform-Specific Notes

### Windows
- Use raw strings for paths: `r"C:\Users\Name\Downloads"` (note the `r` prefix)
- Run from Command Prompt or PowerShell
- Python must be in PATH (check "Add Python to PATH" during installation)
- Example paths: `r"D:\Scripts\"`, `r"C:\Tools\"`, `r"E:\My Folder\"`

### Mac/Linux
- Use forward slashes: `/Users/Name/Downloads`
- Can use `~` for home directory: `~/Downloads`, `~/Documents`
- May need to run with `python3` instead of `python`
- Can make executable with `chmod +x file_manager_pro.py`
- Example paths: `~/scripts/`, `/opt/tools/`, `/usr/local/bin/`

> **Remember:** All paths shown are examples. The script works with **any valid path** on your system.

## Testing

Run the included test suite:

```bash
# Install pytest (optional)
pip install pytest

# Run tests
pytest test_file_manager.py -v
```

## How It Works

1. **Scan:** Recursively scans the target directory
2. **Categorize:** Groups files by size thresholds
3. **Filter:** Applies configured filters and exclusions
4. **Organize:** Moves files to appropriate folders
5. **Log:** Records all operations with timestamps

Files smaller than 1MB are never moved, keeping your directory clean while organizing only larger files.

## Common Questions

**Q: Can I organize folders other than Downloads?**  
A: **Yes!** You can organize ANY folder on your system. Examples include Documents, Desktop, project folders, backup directories, external drives, or any custom location. Downloads is used in documentation examples only.

**Q: Does the script need to be in the same location as the folder I'm organizing?**  
A: **No!** The script can be anywhere. For example, the script can be in `D:\Scripts\` while organizing `C:\Users\YourName\Documents\`. They can even be on different drives.

**Q: Can I use this on an external drive?**  
A: **Yes!** Works on external drives, network drives, or any accessible location.

**Q: Will small files be deleted?**  
A: **No!** Files smaller than 1MB remain in their original location and are never moved.

**Q: Can I change what "large" and "medium" mean?**  
A: **Yes!** Edit the `SIZE_THRESHOLD_MB` and `SIZE_THRESHOLD_GB` values in the configuration section.

## Safety Features

- **Dry-run mode:** Preview changes before execution
- **Backup manifests:** JSON record of original file locations
- **Comprehensive logging:** Track all operations
- **Permission checks:** Validates access before starting
- **Conflict handling:** Automatically renames duplicates
- **Error recovery:** Continues operation on individual file errors

## Troubleshooting

**Python not found:**
- Windows: Reinstall Python and check "Add to PATH"
- Mac: Install via Homebrew: `brew install python3`
- Linux: `sudo apt install python3` (Debian/Ubuntu)

**Permission denied:**
- Windows: Run Command Prompt as Administrator
- Mac/Linux: Check folder permissions with `ls -la`

**Files not moving:**
- Ensure you're not using `--dry-run` flag
- Check FOLDER_PATH is correctly configured
- Verify files meet size threshold (≥ 1MB)

## Author

- **Author:** Eric Jang
- **Email:** thericman05@gmail.com
- **LinkedIn:** Connect me [www.linkedin.com](https://www.linkedin.com/in/eric-jang666/)

## Acknowledgments

Built with Python's standard library - no external dependencies required for core functionality.

⭐ If you find this useful, please consider starring the repository!
