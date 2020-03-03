
import random
from random import randrange

sequence = input("Enter a number of words:")
selection = random.choice(sequence)


def dictionary():
    with open("/usr/share/dict/words", 'r') as dictionary:
        words = dictionary.read().split()
    print(words)


def random_words(amt=selection):
    words = dictionary()
    for _ in range(int(selection)):
        word = randrange(len(words))
        sentence = words[word]
        print(sentence)
        #print(sentence, end=' ')
