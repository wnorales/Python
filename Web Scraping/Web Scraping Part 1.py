import urllib.request
from bs4 import BeautifulSoup

wiki = 'https://en.wikipedia.org/wiki/Computer_science'
page = urllib.request.urlopen(wiki)
soup = BeautifulSoup(page)
