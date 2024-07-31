# Anti-Cheat Application Instructions

## Overview

This document provides instructions for preparing, building, and distributing the Anti-Cheat application. It includes details on how to package the application, run it as a background process, and troubleshoot common issues.

## Files Included

- `Anti_Cheat.exe`: The compiled executable of the application.
- `browser_activity.log` (optional): Log file for tracking browser activity.
- `Anti_cheat.spec`: PyInstaller specification file.

# Installation Instructions for Anti-Cheat Application

## Overview

These instructions guide you through the process of installing and running the Anti-Cheat application on a target system. The application is distributed as a standalone executable and can be run as a background process.

## Prerequisites

1. **Python Installation**: Ensure that Python is installed on the target system.
2. **Required Libraries**: Ensure that the following Python libraries are installed:
   - `psutil`
   - `pygetwindow`
   - `smtplib`
   - `logging`

   You can install these libraries using `pip`:
### Example:

   ```cmd
   pip install psutil
   ```
   ```
   pip install pygetwindow
   ```
3. **Run the Executable in Background**:
  ```cmd
  cd PATH_TO_YOUR_FILE
  ```
  ```cmd
  start /b Anti_Cheat.exe
  ```

### Give Proper Permissions and add it to the exclusion list