@echo off
pip install gtts
pip install pyglet
pyinstaller --clean --onefile --noconsole -i NONE --name "main" main.py
rmdir /s /q __pycache__
rmdir /s /q build
del /f / s /q main.spec
ren dist output

EXIT /B 1 
