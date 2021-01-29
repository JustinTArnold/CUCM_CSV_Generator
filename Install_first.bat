@echo off
cd /D "%~dp0"
rename *.exe python_installer.exe
start python_installer.exe /quiet PrependPath=1 Include_test=0
echo installing python
timeout /t 5
echo Pyhton Installed
pause
python installer.py
pause

