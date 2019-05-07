import requests
from bs4 import BeautifulSoup
import os
links = ''


def telscrawl(name, rstart, rend):
    global links
    for i in range(rstart, rend + 1):
        wpage = 'https://telegram.me/' + name + '/' + str(i)
        html = requests.get("https://translate.google.com/translate?anno=2&depth=1&rurl=translate.google.com&sl=nl&sp=nmt4&u=" + wpage).text
        soup = BeautifulSoup(html, 'html.parser')
        ifr = soup.find_all('iframe')[0]['src']
        soup = BeautifulSoup(html, 'html.parser')
        ifr = soup.find_all('iframe')[0]['src'] 
        ifr = requests.get(ifr).text
        ifr = BeautifulSoup(ifr, 'html.parser').find('meta', attrs={'http-equiv': 'refresh'})
        ifr = ifr['content'].partition('=')[2]
        pgcon = requests.get(ifr).text
        if pgcon.find('view post') == -1:
            print(wpage)
            links += wpage + os.linesep


print("Enter Channel name:")
name = input()
print("Enter start:")
rstart = input()
rstart = int(rstart)
print("Enter end:")
rend = input()
rend = int(rend)
telscrawl(name, rstart, rend)
resualt = open('resualt.txt', 'w')
resualt.write(links)
resualt.close()
