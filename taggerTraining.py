from pickle import load, dump
from random import randrange
from matplotlib.pyplot import text
import nltk
import inspect

text2 = "The quick brown fox jumps over the lazy dog. This upset the lazy dog. The wooden spoon couldn't cut butter. The spoon shouldn't cut anything. It wouldn't do anything. The wooden spoon couldn’t cut but left emotional scars"
text2 = nltk.sent_tokenize(text2)
for i in range(len(text2)):
    text2[i] = nltk.word_tokenize(text2[i])
for i in range(len(text2)):
    text2[i] = nltk.pos_tag(text2[i])

#Fixes
text2[2][3] = ("couldn","MD")
text2[2][4] = ("'t","RB")
text2[3][2] = ("shouldn","MD")
text2[3][3] = ("'t","RB")
text2[4][1] = ("wouldn","MD")
text2[4][2] = ("'t","RB")
text2[5][3] = ("couldn","MD")
text2[5][4] = ("'t","RB")
text2[5][5] = None
text2[5].remove(None)
t2 = text2

output = open('t2.pkl', 'wb')
dump(t2, output)
output.close()