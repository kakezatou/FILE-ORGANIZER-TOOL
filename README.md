# FILE ORGANIZER TOOL

[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](https://github.com/yourusername/file-organizer-tool)
[![Python](https://img.shields.io/badge/python-3.12.4-brightgreen.svg)](https://www.python.org/downloads/release/python-3124/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

A simple tool that renames files to match their parent folder names and moves them to a new location.


## Description

A simple tool that renames files to match their parent folder names and moves them to a new location.

[English](README.md) | [日本語](README.ja.md)

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [How it Works](#how-it-works)
- [Example](#example)
- [Error Handling](#error-handling)
- [To-Do List](#to-do-list)
- [Version History](#version-history)
- [License](#license)


## Features

* Easy to use: Simple interface with clear buttons and options
* Multiple Extensions: Use .txt:.pdf:.docx format to process different file types
* Folder Search: Automatically checks all subfolders
* Safe Renaming: Adds numbers to filenames to avoid overwriting
* Progress Display: Shows what's happening during the process
* Detailed Log: Shows all copied files

## Installation

1. Download the code
2. Run the program:
    ```bash
    python FILE-ORGANIZER-TOOL.py
    ```


## How to Use

1. Click "Browse" to select your source folder
2. Click "Browse" to select your output folder
3. Type the file extensions you want (like .txt:.pdf)
4. Click "Execute Process" button
5. Check the log window to see results


## How it Works

The tool:
1. Looks in all subfolders in your source folder
3. Creates new files in your output folder
4. Names each new file after its parent folder
5. Adds numbers to avoid overwriting existing files


## Example

Before:
```
Source/
  ├── Project1/
  │   └── document.txt
  └── Project2/
      └── notes.txt
```

After:
```
Output/
  ├── Project1.txt
  └── Project2.txt
```


## Error Handling

The tool checks for:
* Missing folders
* Invalid paths
* Permission problems
* File access errors
* Process errors


## To-Do List


- [ ] Add multiple source folders option
- [ ] Add date filtering
- [ ] Add move files option (not just copy)
- [ ] Save favorite settings
- [ ] Add more search options
- [ ] Add dark mode
- [ ] Keep folder structure option
- [ ] Create Windows/Mac installer
- [ ] Add file preview
- [ ] Add more languages


## Version History

* v0.1.0 (2025-02-01) - First version
* v0.1.1 (2025-04-26) - Added Japanese language support


## License

MIT License - see LICENSE file for details

Last updated: 2025-04-26
