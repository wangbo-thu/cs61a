import requests
import os
import bs4
import re

dirName = 'hw'
os.makedirs(dirName, exist_ok=True)
# url = 'https://cs61a.org/hw/'
url = 'https://cs61a.org/hw/sol-'

for i in range(1, 11):
    # link = 'hw{:02d}/hw{:02d}.zip'.format(i, i)
    link = 'hw{:02d}/hw{:02d}.py'.format(i, i)
    res = requests.get(url + link)
    print('Downloading: {}'.format(os.path.basename(link)))
    res.raise_for_status()
    fileName = os.path.join(dirName, os.path.basename(link))
    with open(fileName, 'wb') as f:
        f.write(res.content)
