import os
import sys
import platform
import subprocess


osname = platform.system()
osuser = os.getlogin()
directory = os.getcwd()
history = []


while True:


    osname = platform.system()
    osuser = os.getlogin()
    directory = os.getcwd()
    recognised = False


    command = input(osuser + '@' + osname + ' >>> ')

    if command == '':
        recognised = True

    if 'cd' in command:
        directory = command.replace('cd', '').strip()
        try:
            os.chdir(directory)
        except:
            print('No such file or directory:', directory)
        recognised = True

    if 'ls' in command:
        print(os.listdir())
        recognised = True

    if command == 'pwd':
        print(directory)
        recognised = True

    if command == 'exit':
        sys.exit()
        recognised = True

    if 'echo' in command:
        echo_string = command.replace('echo', '').strip()
        print(echo_string)
        recognised = True

    if 'mkdir' in command:
        dir_string = command.replace('mkdir', '').strip()
        os.mkdir(dir_string)
        recognised = True

    if 'mkfile' in command:
        filename = command.replace('mkfile', '').strip()
        with open(filename, 'w') as file:
            pass
        recognised = True

    if 'mkread' in command:
        recognised = True
        filename = command.replace('mkread', '').strip()
        try:
            with open(filename, 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print('No such file or directory:', filename)
        except PermissionError:
            print('You do not have the necessary permissions to read that file')

    if 'mkedit' in command:
        filename = command.replace('mkedit', '').strip().split()[0]
        filecontents = command.replace(f'mkedit {filename}', '').strip()
        with open(filename, 'w') as file:
            file.write(filecontents)
        recognised = True

    if 'mkremove' in command:
        recognised = True
        filename = command.replace('mkremove', '').strip()
        try:
            os.remove(filename)
        except FileNotFoundError:
            print('No such file or directory:', filename)
        except PermissionError:
            print('You do not have the necessary permissions to remove that file')

    if command == 'history':
        print(history)
        recognised = True

    if 'python' in command:
        filename = command.replace('python', '').strip()
        try:
            with open(filename) as file:
                exec(file.read())
        except FileNotFoundError:
            print('No such file or directory:', filename)
        except PermissionError:
            print('You do not have the necessary permissions to execute that file')
        recognised = True

    if 'giga' in command:
        recognised = True
        filename = command.replace('giga', '').strip()
        def get_input():

                if platform.system() == 'Windows':
                    os.system('cls')
                elif platform.system() == 'Darwin':
                    os.system('clear')
                elif platform.system() == 'Linux':
                    os.system('clear')

                indentvers = os.get_terminal_size().columns - 49
                indentvers2 = indentvers // 2

                print('-'*os.get_terminal_size().columns)
                print('|',' '*indentvers2,'SatsumaProject Giga Text Editor Version 1.2',' '*indentvers2,'|')
                print('-'*os.get_terminal_size().columns)

                print('|')

                lines = []

                while True:
                    line = input('|')
                    if line.strip() == '#END':
                        break
                    elif line.strip() == '#DEL':
                        if lines:
                            lines.pop()
                            try:
                                print("\033[F\033[K", end="")
                                print("\033[F\033[K", end="")
                            except:
                                print('Last Line Has Been Removed')
                    else:
                        lines.append(line)

                return lines

        indentvers = os.get_terminal_size().columns - 9
        indentvers2 = indentvers // 2

        text = get_input()

        for x in range(3):

            print('')

        print('-'*os.get_terminal_size().columns)
        file = filename
        print(' '*indentvers2+'File Saved As '+file)

        with open(file, 'w') as file:
            for line in text:
                file.write(line + '\n')     

    if 'pip' in command:
        recognised = True
        filename = command.replace('pip', '').strip()

        try:
            subprocess.check_call(["pip", "install", f"{filename}"])
        except:
            try:
                subprocess.check_call(["pip3", "install", f"{filename}"])
            except:
                print('ERROR: Could not install: ', filename)
     




    if recognised == False:
        print('Command', command, 'is not a recognised system command')

    history.append(command)