# note for reader using vim
# use :wq to save and exit vim
# use :set number to set line numbers in vim

import argparse
import requests

parser = argparse.ArgumentParser(description="Default Package Manager for the Deniz Open Source Software Project")

parser.add_argument('-j', '--jpg', type=str, help='Use the default DPM install command for JPG files.')
parser.add_argument('-p', '--png', type=str, help='Use default DPM install command for PNG files.')
parser.add_argument('-i', '--install', type=str, help='Use the DPM application library.')
parser.add_argument('-m', '--macos', type=str, help='Use the DPM application library for MacOS.')

args = parser.parse_args()

if args.jpg:

    package_name = args.jpg
    
    try:

        response = requests.get(package_name)
        
        if response.status_code == 200:

            with open("download.jpg", "wb") as file:
                file.write(response.content)

            print('File Downloaded Using DPM')

        else:
            print('Error: Invalid Link')

    except:
        print('Error: Could Not Download File')

if args.png:

    package_name = args.png
    
    try:

        response = requests.get(package_name)
        
        if response.status_code == 200:

            with open("download.png", "wb") as file:
                file.write(response.content)

            print('File Downloaded Using DPM')

        else:
            print('Error: Invalid Link')

    except:
        print('Error: Could Not Download File')

if args.install:

    package_name = args.install

    if package_name == 'debian-amd64':
        
        try:
            response = requests.get('https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.8.0-amd64-netinst.iso')

            with open('debian.iso', 'wb') as file:
                file.write(response.content)
        except:
            print('Error: could not install debian-amd64 package')
            print('Error: this is probably a problem with the')
            print('Error: wait for a new update and try again')

    elif package_name == 'blackarchlinux-amd64':
                
        try:
            response = requests.get('https://ftp.halifax.rwth-aachen.de/blackarch/iso/blackarch-linux-full-2023.04.01-x86_64.iso')

            with open('blackarch.iso', 'wb') as file:
                file.write(response.content)
        except:
            print('Error: could not install blackarchlinux-amd64 package')
            print('Error: this is probably a problem with the')
            print('Error: wait for a new update and try again')

    elif package_name == 'vivaldi':
    
        try:
            response = requests.get('https://downloads.vivaldi.com/stable/vivaldi-stable_7.0.3495.26-1_amd64.deb')

            with open('vivaldi.deb', 'wb') as file:
                file.write(response.content)
        except:
            print('Error: could not install vivaldi package')
            print('Error: this is probably a problem with the')
            print('Error: wait for a new update and try again')

        


if args.macos:

    package_name = args.macos

    if package_name == 'vivaldi':
        
        try:
            response = requests.get('https://downloads.vivaldi.com/stable/Vivaldi.7.0.3495.26.universal.dmg')

            with open('Vivaldi.7.0.3495.26.universal.dmg', 'wb') as file:
                file.write(response.content)
        except:
            print('Error: could not install Vivaldi package')
            print('Error: this is probably a problem with the')
            print('Error: wait for a new update and try again')
        
    if package_name == 'utm':
        
        try:
            response = requests.get('https://github.com/utmapp/UTM/releases/latest/download/UTM.dmg')

            with open('UTM.dmg', 'wb') as file:
                file.write(response.content)
        except:
            print('Error: could not install UTM package')
            print('Error: this is probably a problem with the')
            print('Error: wait for a new update and try again')

    if package_name == 'balenaetcher':
        
        try:
            response = requests.get('https://github.com/balena-io/etcher/releases/download/v1.19.25/balenaEtcher-1.19.25-arm64.dmg')

            with open('balenaEtcher-1.19.25-arm64.dmg', 'wb') as file:
                file.write(response.content)
        except:
            print('Error: could not install BalenaEtcher package')
            print('Error: this is probably a problem with the')
            print('Error: wait for a new update and try again')

    if package_name == 'steam':
        
        try:
            response = requests.get('https://cdn.fastly.steamstatic.com/client/installer/steam.dmg')

            with open('steam.dmg', 'wb') as file:
                file.write(response.content)
        except:
            print('Error: could not install Steam package')
            print('Error: this is probably a problem with the')
            print('Error: wait for a new update and try again')

    if package_name == 'raspi-imager':
        
        try:
            response = requests.get('https://downloads.raspberrypi.org/imager/imager_latest.dmg')

            with open('imager_latest.dmg', 'wb') as file:
                file.write(response.content)
        except:
            print('Error: could not install Raspi Imager package')
            print('Error: this is probably a problem with the')
            print('Error: wait for a new update and try again')
