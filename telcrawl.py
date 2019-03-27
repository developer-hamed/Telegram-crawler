from urllib.request import urlopen
import os
links = ''


def telscrawl(name, rstart, rend):
    global links
    for i in range(rstart, rend + 1):
        wpage = 'https://telegram.me/' + name + '/' + str(i)
        html = urlopen(wpage).read().decode("utf-8")
        if html.find('View Post') == -1:
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
