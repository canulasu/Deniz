import subprocess
import platform
import os
import socket
import time

filename = 'colorama'

try:
    import colorama
except:
    try:
        subprocess.check_call(["pip", "install", f"{filename}"])
    except:
        try:
            subprocess.check_call(["pip3", "install", f"{filename}"])
        except:
            print('ERROR: Could not install dependencies')


filename = 'psutil'

try:
    import psutil
except:
    try:
        subprocess.check_call(["pip", "install", f"{filename}"])
    except:
        try:
            subprocess.check_call(["pip3", "install", f"{filename}"])
        except:
            print('ERROR: Could not install dependencies')


        
if platform.system() == 'Windows':
    os.system('cls')
elif platform.system() == 'Darwin':
    os.system('clear')
elif platform.system() == 'Linux':
    os.system('clear')

from colorama import Fore, Back, Style, init

init()


indentvers = os.get_terminal_size().columns - 23
indentvers2 = indentvers // 2

print('-'*os.get_terminal_size().columns)
print('|',' '*indentvers2,'Deniz CPU Monitor',' '*indentvers2,'|')
print('-'*os.get_terminal_size().columns)


while True:

    percentage = psutil.cpu_percent(interval=1)
    rounded = round(percentage/10)

    a = os.get_terminal_size().columns
    b = a-6
    c = ' '*b
    if rounded != 0:
        print(Fore.YELLOW + rounded*'|'+c+Fore.BLUE+str(percentage)+'%')
    else:
        b = a-5
        c = ' '*b
        print(Fore.YELLOW + rounded*'|'+c+Fore.BLUE+str(percentage)+'%')
    time.sleep(1)