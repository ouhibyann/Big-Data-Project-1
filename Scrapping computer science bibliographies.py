from bs4 import BeautifulSoup
from urllib.request import urlopen

URL_page = "http://liinwww.ira.uka.de/csbib?query=%2b%28ti:global%20ti:warming%29%20%2byr:%5b2013%20TO%209999%5d&sort=score&results=bibtex"
Page = urlopen(URL_page)
Soup = BeautifulSoup(Page, "html.parser")

# Get the first article + removing tags
docs_with_tags = Soup.find('pre', attrs={'class':'bibtex'})
docs = docs_with_tags.text.strip()
print(docs)


'''
# Writing it in file
file1 = open("Myfile.txt", "a")
file1.write(docs)
'''