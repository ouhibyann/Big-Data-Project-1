from bs4 import BeautifulSoup
from urllib.request import urlopen

URL_page = "http://liinwww.ira.uka.de/csbib?query=%2b%28ti:global%20ti:warming%29%20%2byr:%5b2013%20TO%209999%5d&sort=score&results=bibtex"
Page = urlopen(URL_page)
Soup = BeautifulSoup(Page, "html.parser")

print(Soup)