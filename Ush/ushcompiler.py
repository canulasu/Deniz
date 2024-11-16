import os
import sys
import platform
import subprocess

osname = platform.system()
osuser = os.getlogin()
directory = os.getcwd()
history = []

print('Choose ush file to execute')
choosefile = input('>>> ')

if '.ush' in choosefile:

    with open(choosefile, 'r') as file:


        lines = file.readlines()

        osname = platform.system()
        osuser = os.getlogin()
        directory = os.getcwd()
        recognised = False
        read = 0

        for x in range(10):
            print('')

        for line in lines:

            linetoread = lines[read]

            command = linetoread

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

            if 'pwd' in command:
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

            if 'end' in command:
                for s in range(10):
                    print('')


            if recognised == False:
                print('Command', command, 'is not a recognised system command')

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

            history.append(command)

            read += 1


else:
    print('Incorrect file type!')