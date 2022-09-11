import requests #web
import time #delay
import os #restart program/open torrent client
import re #find magnet link
import sys #restart script
from termcolor import colored #color-coding
from bs4 import BeautifulSoup #web filter
#program that fetches game torrents based on user input, check out readme before using!

#searches website based on game name, sets url to be filtered to search.
os.system('color')
url_base="REPLACE WITH URL"
true_url = input (colored('Name of the game you wish to download:', 'green'))
URL = url_base + true_url
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

#find the name of a game and its url
results = soup.find(class_ = "entry-title")
game = results.find('a')
download_url = game["href"]
    
#game confirmation, reexecute on no, proceed on yes
#print(game_name, end="\n"*2) prints all game names.
print(colored(results.text, 'yellow'))
confirmation = input(colored("Is this the game you wanted? (y/n)", 'green'))
if confirmation == "n":
    print(colored("Try a more specific search term or change punctuation. Reexecuting...", 'red'))
    time.sleep(2)
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
    
#desc = soup.body.findAll(text=re.compile(r'Genres/Tags:.*'))
#print(desc)

#finds magnet link and opens it with torrent client
print (colored("Starting download...", 'cyan')) 
#time.sleep(2.5)
URL = download_url
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
monkey = soup.find('a', href = re.compile(r'magnet.*'))
os.startfile(monkey["href"])
