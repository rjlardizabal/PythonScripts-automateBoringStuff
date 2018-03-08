#! python 3
# lucky.py - Opens severeal Google search results.

import requests, sys, webbrowser, bs4

print('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)

linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))

for i in range(numOpen):
    webbrowser.open('https://google.com'+linkElems[i].get('href'))