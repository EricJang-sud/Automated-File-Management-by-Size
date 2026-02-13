# Automated File Management System by Size

A Python automation tool that organizes thousands of files by size in seconds, eliminating hours of manual work and reducing storage management overhead.

<p align="center">
  <img src="assets/Before-After Gemini.png" width="700" alt="Before and After Comparison">
</p>
<p align="center">
  Image credit: Gemini
</p>

## 🎯 The Problem

You open your Downloads folder 📂: **3,247 files**. **89GB used** 💾. 

Somewhere in there are the large video files 🎥 eating your storage, but finding them means **15 minutes of scrolling** ⏳. 

Manually sorting? **2+ hours** 😵‍💫 of dragging 🖱️, dropping 📥, and second-guessing 🤔.

**This is a common productivity drain across organizations:**
- IT teams waste hours on storage cleanup
- Developers lose time searching for large files
- Project folders become unmanageable
- Critical disk space issues go unnoticed until it's too late

## ✨ The Solution

⚡ **This script solves it in ~4 seconds.**

✅ **What it does:**
- 📦 Large files are automatically organized into size-based folders
- 📁 Small files stay exactly where they are (no unnecessary moves)
- 📝 Every action is logged for a complete audit trail
- 🔄 Includes rollback capability via backup manifests
- 🔍 Preview mode lets you see changes before they happen

## ⏱️ Impact: Before vs After

|                    | ❌ Before (Manual)                         | ✅ After (Automated)                  |
|--------------------|--------------------------------------------|---------------------------------------|
| ⏳ **Time Required**    | ~2 hours for 3,000+ files                 | **~4 seconds**                        |
| 🧠 **Effort**           | High cognitive load, tedious              | **One command**                       |
| ⚠️ **Error Risk**       | Human error, missed files                 | **100% accurate**                     |
| 🔍 **Visibility**       | Manual inspection, guesswork              | **Instant categorization**            |
| 📝 **Audit Trail**      | None                                      | **Full logging**                      |
| 💰 **Cost Impact**      | Developer time burned on cleanup          | **Automated, repeatable**             |
| ☕ **Developer Time**   | Wasted on manual tasks                    | **Available for value-add work**      |

## 🛠️ About The Tool

This tool automatically categorizes and organizes files in **any folder** based on configurable size thresholds:

**Default Organization:**
- **Files ≥ 1GB** → `above 1GB` folder
- **Files 1MB-1GB** → `1MB-1GB` folder
- **Files < 1MB** → Remain in original location (untouched)

> All thresholds are fully customizable to meet your team's needs.

## 💼 Business Use Cases

This automation tool is applicable across industries where teams manage large volumes of digital files:

- :white_check_mark: **IT & Technology** – Managing logs, downloads, backups, and system storage directories  
- :white_check_mark: **Data & Analytics** – Organizing datasets, exports, and large research files for easier access  
- :white_check_mark: **Corporate & Office Environments** – Maintaining clean shared drives, project folders, and reporting assets  
- :white_check_mark: **Creative & Media Industries** – Structuring large video, image, and production files for faster retrieval  
- :white_check_mark: **General Productivity Users** – Keeping personal or shared folders organized while reducing digital clutter  


## 🎨 Key Features

The following key features highlight the tool’s core capabilities, usability, and reliability in organizing files efficiently across different IT environments.

### Core Functionality
- 🎯 **Intelligent Categorization** - Automatically sorts by configurable size thresholds
- 📊 **Real-time Analytics** - File type distribution, size statistics, processing metrics
- 📝 **Comprehensive Logging** - Full audit trail with timestamps and operation details
- 🔍 **Dry-run Mode** - Preview all changes before execution (risk-free testing)

### User Experience
- 🎛️ **Flexible Configuration** - All settings in one easy-to-edit section
- 💬 **Interactive CLI** - User-friendly command-line interface
- 📦 **Zero Dependencies** - Uses only Python standard library
- 🌍 **Cross-platform** - Windows, macOS, Linux compatible

## 📸 Proof of Results

An example of demonstrating how the automation reorganises a cluttered folder by automatically grouping large files into clearly labelled size-based directories while leaving smaller files untouched.

### Before: Chaos
```
Downloads/
├── vacation_video_final_v3.mp4 (2.5 GB)
├── work_presentation_draft.pptx (45 MB)
├── screenshot_1.png (800 KB)
├── dataset_large.csv (1.2 GB)
├── photo_backup.zip (3.8 GB)
├── meeting_notes.txt (5 KB)
├── random_file.pdf (150 KB)
└── ... 3,240 more files
```

### After: Organized
```
Downloads/
├── above 1GB/
│   ├── vacation_video_final_v3.mp4 (2.5 GB)
│   ├── dataset_large.csv (1.2 GB)
│   └── photo_backup.zip (3.8 GB)
├── 1MB-1GB/
│   └── work_presentation_draft.pptx (45 MB)
├── screenshot_1.png (800 KB)        ← Stayed in place
├── meeting_notes.txt (5 KB)         ← Stayed in place
├── random_file.pdf (150 KB)         ← Stayed in place
└── ... all small files remain here
```

**Result:** 
- ✅ **7.5 GB** of large files immediately visible and organized
- ✅ **3 folders** created automatically with clear naming
- ✅ **3,244 small files** left undisturbed in original locations
- ✅ **Complete log** of all operations saved

## 💡 Roles & Skills Demonstrated

This project reflects practical skills relevant to data analytics, operations, and business-focused technical roles:

- **Data handling & automation:** Built a solution that processes thousands of files efficiently and consistently  
- **Problem solving:** Identified a common productivity issue and designed a scalable, repeatable solution  
- **Analytical thinking:** Measured performance improvements and translated results into business impact metrics  
- **Process improvement mindset:** Reduced manual work through automation and structured workflows  
- **Documentation & communication:** Created clear, user-focused documentation for both technical and non-technical users  

## 🚀 Quick Start

### What You Need:
- A laptop or desktop 
- Python 3.6 or higher installed
- A folder you want to organize
- 5 minutes of your time
- An external hard drive (optional)

### What Happens:
1. Download the script
2. Edit one line to set your target folder
3. Run one command
4. Watch your files get organized in seconds

*Full technical instructions are in [Technical Documentation](Technical-Documentation.md).*

## 📞 Author

1. **Author:** Eric Jang
2. **Email:** thericman05@gmail.com
3. **LinkedIn:** Connect me [www.linkedin.com](https://www.linkedin.com/in/eric-jang666/)

## 🙏 Acknowledgments

Built with Python's excellent standard library. No external dependencies required for core functionality.

**⭐ If you find this useful, please consider starring the repository!**

---

**Ready to implement?** See [Technical Documentation](Technical-Documentation.md) for complete setup instructions.
