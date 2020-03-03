import sys
import random
import string
from numpy.random import choice


def histogram(fileName):
    textFile = open(fileName, "r")
    fileLines = textFile.readlines()
    histogram = {}

    for line in fileLines:
        for word in line.split():
            # strip punctuation/capitals
            i = word.lower().translate(
                str.maketrans('', '', string.punctuation))
            if i in histogram:
                histogram[i] = histogram[i] + 1
            else:
                histogram[i] = 1

    return histogram


def unique_words(fileName):
    return len(histogram(fileName))


def frequency(fileName, target):
    return histogram(fileName)[target]


def sample(fileName):
    return random.choice(list(histogram(fileName).keys()))


def words1(fileName, sampleCount=1):
    hist = histogram(fileName)

    # number of (total, not unique, words)
    word_count = 0
    for key in hist:
        word_count += hist[key]

    probability_list = []
    for key in hist:
        probability_list.append(hist[key]/word_count)

    weighted_choice = choice(list(histogram(fileName).keys()), sampleCount,
                             p=probability_list)
    # print(list(histogram(fileName).keys()))
    # print(probability_list)
    return weighted_choice


def sentence(fileName, word_count=9, sentenct_structure=True):
    """weighted sampling"""
    phrase = ""
    words = words1(fileName, word_count)
    for word in words:
        phrase += word + " "
    phrase = phrase.strip()
    if sentenct_structure:
        phrase = phrase.capitalize()
        phrase += "."
    return phrase


if __name__ == '__main__':
    # print(unique_words(str(sys.argv[1])))
    print(frequency(str(sys.argv[1]), str(sys.argv[2])))
    print(sample(str(sys.argv[1])))
    print(words1(str(sys.argv[1])))
    test_weight(str(sys.argv[1]), 200000)
