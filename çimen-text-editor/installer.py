# You may be wondowering what this script is. It is an installerfor turning the source code
# of the Çimen Text Editor to an executable file. Note, it may not work on Windows computers.

import os
import platform
os.system('pip3 install pyinstaller')
os.system('pip install pyinstaller')
os.system('pyinstaller --windowed --noconsole source.py')
os.system('rm source.spec')
os.system('rm -rf build')
os.chdir('dist')
if platform.system() == 'Darwin':
    os.system('mv source.app ../')
if platform.system() == 'Windows':
    os.rename('source.exe', '../source.exe')
if platform.system() == 'Linux':
    os.system('mv source ../')
os.chdir('..')
os.system('rm -rf dist')