
import random
from random import randrange

sequence = [i for i in range(3,10)]
selection = random.choice(sequence)


def dictionary():
    with open("/usr/share/dict/words", 'r') as dictionary:
        words = dictionary.read().split()
    return words


def random_words(amt=selection):
    words = dictionary()
    for _ in range(int(selection)):
        word = randrange(len(words))
        sentence = words[word]
        print(sentence, end=' ')
