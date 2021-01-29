import subprocess
import os
from os import listdir, mkdir
from os.path import isfile, join
import time

my_path = "./"
all_files = [f for f in listdir(my_path) if isfile(join(my_path, f))]
os.remove('python_installer.exe')

try:
	my_path = os.path.join('./', 'csv_templates')
	os.mkdir(my_path)
	print ("csv_templates directory created")
except:
	print ("csv_templates directory already exists")
time.sleep(1)
for each in all_files:
	if each.endswith('csv'):
		os.rename(each, f'./csv_templates/{each}')
print('moved all csv template files')
time.sleep(1)
try:
	my_path = os.path.join('./', 'output')
	os.mkdir(my_path)
	print ("output directory created")
except:
	print ("output directory already exists")
time.sleep(1)
try:
	my_path = os.path.join('./', 'update_files')
	os.mkdir(my_path)
	print ("update_files directory created")
except:
	print ("update_files directory already exists")
time.sleep(1)
print ("installing dependencies")
time.sleep(2)
for each in ('pyqt5', 'numpy', 'pandas', 'sys', 'datetime', 'wget'):
	subprocess.run(f'pip install {each}')
print('all dependencies installed: hopefully')
break_line = input("<<<Press any key to exit>>>")



