#!/usr/bin/python3

# required libraries
import nltk
from nltk import word_tokenize, sent_tokenize
statement1="Vishal is good boy"
out1=word_tokenize(statement1)         # to tokenize the words 
print(out1)


statement2="vishal is cool. he is calm and composed in nature."
out2=sent_tokenize(statement2)    # to tokenize sentences
print(out2)
