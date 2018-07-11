#!/usr/bin/python3



from bs4 import BeautifulSoup                        # libraries which need to imported     
import nltk
import urllib.request
from nltk.corpus import stopwords

crawl=urllib.request.urlopen("https://python.org")   # to request the data from website
html=crawl.read()
print(html)                                          # text contain includes a lot  of html tags
print("-----------------------------------------------------------------------------------------------------------------------------")
soup_data=BeautifulSoup(html,'html5lib')             #'html5lib' is the parser to remove html tags
print(soup_data)
print("-----------------------------------------------------------------------------------------------------------------------------")
clean=soup_data.get_text(strip=True)                 # to extract only text
print(clean)
print("-----------------------------------------------------------------------------------------------------------------------------")
tokens=clean.split()
print(tokens)
print("-----------------------------------------------------------------------------------------------------------------------------")
tokenized=[i for i in tokens]
print(tokenized)

count=nltk.FreqDist(tokenized)
print(count)
count.plot(10)
for key,val in count.items():
		print(str(key) +":"+ str(val))





