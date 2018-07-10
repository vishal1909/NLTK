#!/usr/bin/python3
import nltk


from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
 


sentence="Example: Given a product review, a computer can predict if its positive or negative based on the text."
sent=sent_tokenize(sentence)

for s in sent :
    #print(nltk.pos_tag((word_tokenize(s))))
    l=nltk.pos_tag((word_tokenize(s)))
#print(l) 
for i in l:
    if 'NN' in i[1]:
        print(i)
          
