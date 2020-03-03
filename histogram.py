from sourcetxt import source_txt

text = source_txt.split(" ")
words = []
for word in text:
    words.append(word)

def frequency(word):
        frequency = words.count(word)
        return frequency

def histogram(word):
    histogram_dict = {}
    hist2 = []
    for word in words:
        if word in histogram_dict:
            pass
        else:
            histogram_dict[word] = frequency(word)
            hist2.append((word,frequency(word)))
    #print(hist2)
    return(hist2)



def unique_words():
    ''' Take a histogram and return the number of unique words'''
    unique = histogram(str(text))
    for i in unique:
        lst = (i[0])
    print(int(len(lst)+1))
