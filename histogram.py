from sourcetxt import source_txt

text = source_txt.split(" ")
words = []
for word in text:
    words.append(word)

def histogram(word):
        frequency = words.count(word)
        return frequency

def unique_words(word):
    unique_words_list = []
    amount = words.count(word)
    if amount == 1:
        unique_words_list.append(word)
    return unique_words_list
