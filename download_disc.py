import requests
import os
import bs4
import re

dirName = 'disc'
os.makedirs(dirName, exist_ok=True)
url = 'https://cs61a.org/'
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.content, 'html.parser')
slides = soup.find_all('a', {'href': re.compile('disc\/.*\.pdf')})
uniqueSlides = sorted(set(slides), key=lambda x: x.get('href'))
for slide in uniqueSlides:
    print(os.path.basename(slide.get('href')))

for slide in uniqueSlides:
    print('Downloading...')
    link = slide.get('href')
    res = requests.get(url + link)
    print(os.path.basename(link))
    res.raise_for_status()
    fileName = os.path.join(dirName, os.path.basename(link))
    with open(fileName, 'wb') as f:
        f.write(res.content)
