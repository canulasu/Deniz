import os
import platform
import subprocess

if platform.system() == 'Windows':
    os.system('cls')
elif platform.system() == 'Darwin':
    os.system('clear')
elif platform.system() == 'Linux':
    os.system('clear')

indentvers = os.get_terminal_size().columns - 29
indentvers2 = indentvers // 2
print('-'*os.get_terminal_size().columns)
print('|',' '*indentvers2,'Deniz Package Installer',' '*indentvers2,'|')
print('-'*os.get_terminal_size().columns)

print('')
print('Choose Package Type')
print('')
print('1) Python Package')
print('')
type = input('>>> ')
print('')

if type == '1':
    print('Please Input Package Name')
    command = input('>>> ')
    filename = command

    try:
        subprocess.check_call(["pip", "install", f"{filename}"])
    except:
        try:
            subprocess.check_call(["pip3", "install", f"{filename}"])
        except:
            print('ERROR: Could not install: ', filename)
else:
    print('Package type "'+type+'" is not a recognised package type')