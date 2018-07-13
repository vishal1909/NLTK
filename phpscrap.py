#!/usr/bin/python3

import nltk
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import urllib.request

crawler=urllib.request.urlopen("https://php.net")
htmltags=crawler.read()
souped=BeautifulSoup(htmltags,'html5lib')
data=souped.get_text(strip=True)
l=[]
for i in data.split():
	if i not in stopwords.words('english'):
		l.append(i)

print(len(l))


r=[]
for i in data.split():
	r.append(i)
print(len(r))


count=nltk.FreqDist(l)
count.plot(30)
for key,val in count.items():
	print(str(key) +":" + str(val))

count=nltk.FreqDist(r)
count.plot(30)


