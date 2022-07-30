from matplotlib.pyplot import get

from general import getSentanceENG


def combineNouns(sentance, flag):
    if flag:
        i = 1
        while i <= (len(sentance)-2):
            if sentance[i].typeArb == sentance[i+1].typeArb and sentance[i].typeArb[0]  == "N":
                sentance[i].word = sentance[i].word + " " + sentance[i+1].word
                sentance.pop(i+1)
            i = i + 1 
    return sentance

def isNoun(data):
    if data.typeArb[0] == "N" or data.typeArb == "PRP" or data.typeArb == "PRP$" or data.typeArb == "WP" or data.typeArb == "WP$":
        return True
    else:
        return False

def isPronoun(data):
    if data.typeArb[:3] == "PRP":
        return True
    else:
        return False

def isProperNoun(data):
    if data.typeArb == "NNP":
        return True
    else:
        return False