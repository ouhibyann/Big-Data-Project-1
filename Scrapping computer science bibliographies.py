from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

URL_page = "http://liinwww.ira.uka.de/csbib?query=%2b%28ti:global%20ti:warming%29%20%2byr:%5b2013%20TO%209999%5d&sort=score&results=bibtex"
Page = urlopen(URL_page)
Soup = BeautifulSoup(Page, "html.parser")

# Get the first article + removing tags
docs_with_tags = Soup.find_all('pre', class_='bibtex')

docs = docs_with_tags.text.strip()


# Writing it in file and cleaning it -without the '@Article'.
def cleaning():
    file1 = open("Myfile.txt", "w+")
    clean_file1 = open("cleaned_file1.txt", "w+")
    lst = []
    file1.truncate(0)
    file1.write(docs_with_tags)
    for line in docs_with_tags:
        lst.append(line)
    del lst[0:8]
    # print(lst)
    file1.close()
    for i in range(len(lst)):
        clean_file1.write(lst[i])
    clean_file1.close()


# The authors are split by the key word 'and'.
