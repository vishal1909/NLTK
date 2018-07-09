#!/usr/bin/python3


import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize ,sent_tokenize

statement="His office issued an official statement concerning his departure.This is his first public statement about the investigation.I disagree with your earlier statement about my record on this issue.The advertisement included misleading statements about the product.The police took the witness's statement."

tokenize=word_tokenize(statement)
print(tokenize)

filter=[]
for w in tokenize:
    if w not in stopwords.words('english'):
        filter.append(w)
print(filter)  

print("With Stopwords:",+len(tokenize))
print("Without Stopwords:",+len(filter))
        