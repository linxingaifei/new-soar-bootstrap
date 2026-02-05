@echo off
pip install -r requirements.txt
pip install pyinstaller
pyinstaller --onefile main.py
echo Build complete. See dist\main.exe
