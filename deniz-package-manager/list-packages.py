import os
import platform
import subprocess
import sys

if platform.system() == 'Windows':
    os.system('cls')
elif platform.system() == 'Darwin':
    os.system('clear')
elif platform.system() == 'Linux':
    os.system('clear')

print('Installed Packages:')
print('')
try:
    print(subprocess.check_output([sys.executable, "-m", "pip", "list"]))
except:
    print(subprocess.check_output([sys.executable, "-m", "pip3", "list"]))
