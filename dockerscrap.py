#!/usr/bin/python3 

# libraries
import nltk
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import urllib.request


# to read the data
crawler = urllib.request.urlopen("https://www.docker.com")
html=crawler.read()   # data contains a lot of html tags.
#print(html)
data=BeautifulSoup(html,'html5lib')              # parse using html5lib parser
clean=data.get_text(strip=True)
split=[i for i in clean.split() if  i not in stopwords.words()]      # removing stopwords

splitter=[i for i in clean.split()]
#print(split)
count=nltk.FreqDist(split)                          # freq of samples
print(count)
count.plot(10)                        			# plotting top 10 on graph
for key,val in count.items():
		print(str(key) +":"+ str(val))

print(len(split))
print(len(splitter))

		

