---
name: reference-python-DJB_HOME_TOWER
description: Python path on DJB_HOME_TOWER — Anaconda, not on system PATH
metadata:
  type: reference
  machine: DJB_HOME_TOWER
---

On DJB_HOME_TOWER, Python is installed via Anaconda at `C:\Users\james\anaconda3\python.exe`. It is not on the system PATH, so `python` or `python3` commands fail in the terminal. Always invoke as `& "C:\Users\james\anaconda3\python.exe"` in PowerShell. Pillow (PIL) is available in the base environment.
