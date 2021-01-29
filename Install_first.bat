cd /D "%~dp0"
rename *.exe python_installer.exe
start python_installer.exe /quiet PrependPath=1 Include_test=0
echo Pyhton Installed
pause
start installer.py

