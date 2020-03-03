from sourcetxt import source_txt
from python_quote import random_python_quote
from rearrange import rearrange
#from sentence import random_words
from histogram import unique_words
from histogram import histogram
from histogram import frequency
from listogram import listogram


text = source_txt.split(" ")
words = []
for word in text:
    words.append(word)

#print(random_python_quote()) #REARRANGE #will return a random quote from list in tutorial
#print(histogram(str(text))) # HISTOGRAM returns a list of tuples and in word,frequency format
#unique_words() UNIQUE WORDS#will return the number of unique words in a text
#print(rearrange("the cow jumped over the moon")) #takes in a sting as a parameter and rearranges
#print(frequency("fish")) #will return the frequency of a word in a given text
print(listogram)

#random_words() # DICTIONARY WORDS takes random words from words library and returns them
