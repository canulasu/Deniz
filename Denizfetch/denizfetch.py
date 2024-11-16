import subprocess
import platform
import os
import socket

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


        
if platform.system() == 'Windows':
    os.system('cls')
elif platform.system() == 'Darwin':
    os.system('clear')
elif platform.system() == 'Linux':
    os.system('clear')

from colorama import Fore, Back, Style, init

init()

print(Fore.YELLOW + platform.node())
print(Style.RESET_ALL+'-'*len(platform.node()))
print(Fore.YELLOW + 'OS'+ Style.RESET_ALL+': '+platform.system())
print(Fore.YELLOW + 'Host'+ Style.RESET_ALL+': '+socket.gethostname())
print(Fore.YELLOW + 'Kernel'+ Style.RESET_ALL+': '+platform.system())
print(Fore.YELLOW + 'Shell'+ Style.RESET_ALL+': '+os.getenv('SHELL'))
print(Fore.YELLOW + 'CPU'+ Style.RESET_ALL+': '+platform.processor())