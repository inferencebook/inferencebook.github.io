---
name: feedback-notebook-edits
description: How to edit Jupyter notebooks in this repo — always use Python scripts, never NotebookEdit
metadata:
  type: feedback
  machine: all
---

Always edit notebooks via temporary Python scripts run with the Anaconda Python executable. Never use the NotebookEdit tool — it fails with "file modified since read" errors.

**Why:** NotebookEdit conflicts with the file state tracking; Python scripts with `json.load/dump` are reliable.

**How to apply:** Write a `.py` script, run it, then delete it. Always use `encoding='utf-8'` on `open()` and `ensure_ascii=False` on `json.dump()` to avoid mojibake. See [[reference-python-DJB_HOME_TOWER]] for the Python path on the home tower.
