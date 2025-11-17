# Data Track Python Practice

This repository contains the GLOCAL Data Track Python Practice exercise.

You will complete short coding tasks in `glocal_practice.py`, verify your work with `run_to_verify.py`, and then submit your finished file through Google Drive.

---

## 1. Install Python

If you do not already have Python installed:

**Windows**
1. Go to https://www.python.org/downloads/
2. Click "Download Python"
3. During installation, check "Add Python to PATH" before clicking "Install Now"

**Mac**
1. Open Terminal and type:
   ```bash
   python3 --version
    ```

2. If you do not see a version number, download and install Python from [https://www.python.org/downloads/](https://www.python.org/downloads/)

---

## 2. Get the Practice Files

**Option A: Download as ZIP**

1. Click the green "Code" button on this page.
2. Select "Download ZIP".
3. Unzip the folder to your computer.

**Option B: Clone using Git**
If you are comfortable with Git:

```bash
git clone https://github.com/Glocal-Open-Source/python-problem-sets.git
```
---

## 3. Open the Folder

1. Open Visual Studio Code (VS Code).
2. Go to **File → Open Folder...**
3. Select the unzipped folder.
4. You should see these files:

   ```
   glocal_practice.py
   run_to_verify.py
   README.md
   ```

---

## 4. Complete the Exercises

Open `glocal_practice.py` and complete each function by replacing the `# TODO` comments with code.

Example:

```python
def extract_page_numbers():
    text = "Page 123 of 456"
    # TODO: extract both numbers and return them as a tuple of ints
    return None
```

Becomes:

```python
def extract_page_numbers():
    text = "Page 123 of 456"
    parts = text.split()
    return int(parts[1]), int(parts[3])
```

Save your changes as you go. If you ever get stuck, run `run for hints` to solve basic arithmetic in python terminal to receive hints.

---

## 5. Verify Your Work

To test your answers, open a terminal in VS Code and run:

```bash
python run_to_verify.py
```

The output will show which tasks passed or failed. Example:

```
[PASS] extract_page_numbers
[FAIL] reverse_string — got 'LACOGL' expected 'LACOLG'
```

Fix any failing functions in `glocal_practice.py` until all tasks pass.

If you see:

```
You haven’t started in glocal_practice.py (everything returned None).
```

It means you have not edited any functions yet.

---

## 6. Submit Your Work

1. Find your completed `glocal_practice.py` file.
2. Upload it to your Google Drive.
3. Right-click the file and select "Share".
4. Set link sharing to "Anyone with the link" (Viewer access).
5. Copy the link.
6. Submit the link as your final submission using PY01 as the submission code and 120 hours 

---

## 7. Troubleshooting

**Problem:** "python not found"
**Fix:** Reopen VS Code after installation or try `python3` instead of `python`.

**Problem:** "run_to_verify.py not found"
**Fix:** Ensure you are in the same folder as both files before running the command.

---

## Summary

| Step | Action                                                      |
| ---- | ----------------------------------------------------------- |
| 1    | Install Python                                              |
| 2    | Download or clone this repository                           |
| 3    | Open the folder in VS Code                                  |
| 4    | Complete `glocal_practice.py`                               |
| 5    | Run `run_to_verify.py` to test your code                    |
| 6    | Upload your solved file to Google Drive and submit the link |


---

