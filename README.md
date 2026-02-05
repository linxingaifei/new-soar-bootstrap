# SOAR Bootstrap (Python)

## Quick Test
```
pip install -r requirements.txt
python main.py --dry-run
python main.py --lang=en --dry-run
```

## Build EXE (Windows)
```
pip install pyinstaller
pyinstaller --onefile main.py
```
Output: dist/main.exe (rename to Bootstrap.exe)
