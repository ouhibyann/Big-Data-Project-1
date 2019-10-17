from bs4 import BeautifulSoup
from urllib.request import urlopen

URL_page = "https://liinwww.ira.uka.de/bibliography/index.html"
Page = urlopen(URL_page)
Soup = BeautifulSoup(Page, "html.parser")

print(Soup)