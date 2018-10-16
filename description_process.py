import pandas as pd
import nltk
import os
import re
import numpy as np
from matplotlib import pyplot as plt

# nltk.download()

log = pd.read_csv("out.csv",engine = "python", delimiter="\t")
# the number of every module
moduleNum = log.groupby('Module').size()
# the number of operator server
OnameNum = log.groupby('Oname').size()
# the number of different descriptions
description = log.groupby('Msg').size()

#text analysis: include preprocess, word frequency, tf-idf
# extract description msg
des = log['Msg']
i = 0
s = ""
for i in range(len(des)):
    s = s+des[i]

#import stopwords
stopWords = nltk.corpus.stopwords.words("english")
#import punctuations
english_punctuations = [',', '.', ':', '=', '>', '@','|', ';', '?', '(', ')', '/', '[', ']', '!', '@', '#', '%', '$', '*', '\n']
# remove puctuations
for ch in s:
    if ch in english_punctuations:
        s = s.strip(ch)
# split words
splitWords = nltk.word_tokenize(s)
# remove stopwords
for word in splitWords:
    if word in stopWords:
        splitWords.remove(word)

# count word frequency
fredist = nltk.FreqDist(splitWords)
print(fredist)
# words only appear one time
fredist.hapaxes()

# bigrams
# extract pairs of neighbor words
bipairs = nltk.bigrams(splitWords)

# possible features
# length of total description string
descripLength = [len(msg) for msg in des]

# number of words of each description
numOfWords = [len(nltk.word_tokenize(msg)) for msg in des]

# histogram over the characters
bins = np.arange(0, max(descripLength), 1)
data = np.array(descripLength)
plt.hist(data, bins)
plt.title("histogram over the characters of description")
plt.xlabel("count")
plt.ylabel("length of description")
plt.show()