from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
 
words = ["sports","sport","sportfreak","sporting"]
ps = PorterStemmer()              # stemming is done to obtain the root word.
 
for word in words:
    print(word + ":" + ps.stem(word))
    
