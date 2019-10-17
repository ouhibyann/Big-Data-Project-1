from bs4 import BeautifulSoup
from urllib.request import urlopen

URL_page = "http://liinwww.ira.uka.de/csbib?query=%2b%28ti:global%20ti:warming%29%20%2byr:%5b2013%20TO%209999%5d&sort=score&results=bibtex"
Page = urlopen(URL_page)
Soup = BeautifulSoup(Page, "html.parser")

# Get the first article + removing tags
docs_with_tags = Soup.find('pre', attrs={'class':'bibtex'})
docs = docs_with_tags.text.strip()


# Writing it in file and cleaning it -without the '@Article'.
file1 = open("Myfile.txt", "w+")
clean_file1 = open("cleaned_file1.txt", "w+")
lst = []
file1.truncate(0)
file1.write(docs)
for line in docs:
    lst.append(line)
del lst[0:8]
# print(lst)
file1.close()
for i in range(len(lst)):
    clean_file1.write(lst[i])
clean_file1.close()
