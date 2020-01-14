import requests
import os
import bs4
import re

dirName = 'lab'
os.makedirs(dirName, exist_ok=True)
url = 'https://cs61a.org/'
# url = 'https://cs61a.org/hw/sol-'

for i in range(4, 15):
    # link = 'hw{:02d}/hw{:02d}.zip'.format(i, i)
    link = '{}/{}{:02d}/{}{:02d}.zip'.format(dirName, dirName, i, dirName, i)
    res = requests.get(url + link)
    print('Downloading: {}'.format(os.path.basename(link)))
    try:
        res.raise_for_status()
    except Exception as ex:
        print(ex.msg)
    fileName = os.path.join(dirName, os.path.basename(link))
    with open(fileName, 'wb') as f:
        f.write(res.content)
