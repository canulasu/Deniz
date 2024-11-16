import argparse
import subprocess

filename = 'wikipedia-api'

try:
    import wikipediaapi
except:
    try:
        subprocess.check_call(["pip", "install", f"{filename}"])
    except:
        try:
            subprocess.check_call(["pip3", "install", f"{filename}"])
        except:
            print('ERROR: Could not install dependencies')

wiki = wikipediaapi.Wikipedia(
    language = 'en',
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent= 'smallwiki (Python/3.12.2; Contact: jakarandainnovation@gmail.com; Purpose: Making Wikipedia client for small operating systems!)'
)

parser = argparse.ArgumentParser(description="SmallWiki is a Wikipedia Client for small operating systems.")

parser.add_argument('-s', '--search', type=str, help='Search for an article on Wikipedia!')
parser.add_argument('-d', '--download', type=str, help='Search and download an article on Wikipedia!')
parser.add_argument('-f', '--full', type=str, help='Search and download a full article on Wikipedia!')
parser.add_argument('-e', '--spanish', type=str, help='Search and download a full article on Wikipedia!')
parser.add_argument('-i', '--information', action='store_true', help='Information about SmallWiki')


args = parser.parse_args()



if args.search:
    search = args.search
    page = wiki.page(search)
    if page.exists():
        print('Page summary found on Wikipedia using SmallWiki:')
        print(' ')
        print(' ')
        print(' ')
        print(page.summary)
        print(' ')
        print(' ')
        print(' ')
    else:
        print(' ')
        print(f'Sorry, SmallWiki could not find the article you are looking for!')
        print(f'For more information, visit https://www.wikipedia.org')
        print(' ')

if args.full:
    search = args.full
    page = wiki.page(search)
    if page.exists():
        print('Full page found on Wikipedia using SmallWiki:')
        print(' ')
        print(' ')
        print(' ')
        print(page.text)
        print(' ')
        print(' ')
        print(' ')
    else:
        print(' ')
        print(f'Sorry, SmallWiki could not find the article you are looking for!')
        print(f'For more information, visit https://www.wikipedia.org')
        print(' ')

if args.download:
    search = args.download
    page = wiki.page(search)
    if page.exists():
        print('Page summary found on Wikipedia and downloaded using SmallWiki:')
        print(' ')
        print(' ')
        print(' ')
        file = open('article.txt', 'w')
        file.write(page.summary)
        file.close()
        print(' ')
        print(' ')
        print(' ')
    else:
        print(' ')
        print(f'Sorry, SmallWiki could not find the article you are looking for!')
        print(f'For more information, visit https://www.wikipedia.org')
        print(' ')


if args.information:
    print('The SmallWiki Wikipedia client is a Wikipedia client for headless operating systems or people who want to use Wikipedia on their terminal or command line.')