from re import I
import nltk
from nltk.tokenize.stanford import StanfordTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import NgramTagger
from nltk.corpus import stopwords
from pickle import load
from sentanceAnalysis import *
from general import *
from general import text2
from nouns import combineNouns, isNoun, isPronoun, isProperNoun
from adjective import isAdj
from adverb import isAdverb
from verb import isVerb
from coReferenceModelCreation import nlp

stop_words = (set(stopwords.words('english')))

def prepareText(para,stopWordFlag):
    para = para.replace("\n"," ")
    para = deAbreviate(para)
    global textForChaining
    textForChaining = para
    para = splitTextSen(para)
    para = tokenizeText(para)
    para = removeStopWords(para, stopWordFlag)
    para = taggingText(para)
    para = instantiationText(para)
    return para

def splitTextSen(text):
    text = sent_tokenize(text)
    return text

def tokenizeText(text):
    for i in range (len(text)):
        text[i] = nltk.word_tokenize(text[i])
    return text

def removeStopWords(text, flag):
    if flag:
        stop_words = (set(stopwords.words('english')))
        for i in range(len(text)):
            filtered = [w for w in text[i] if not w.lower() in stop_words]
            text[i] = filtered
    return text

def deAbreviate(text):
    if "'" in text:
        if "n't" in text:
            text = text.replace("n't"," not")
            text = text.replace(" ca "," can ")
        text = text.replace("'ve"," have")
        text = text.replace("'m"," am")
        text = text.replace("n't've"," not have")
        text = text.replace("it's","it is")
        text = text.replace("It's","It is")
        text = text.replace(" he's"," he is")
        text = text.replace("He's","He is")
        text = text.replace(" she's"," she is")
        text = text.replace("She's","She is")
        text = text.replace("'d"," had")
    return text

def taggingText(text):
    # Use to train own tagger
    # t0 = NgramTagger()
    # input = open('t1.pickle', 'rb')
    # t1Data = load(input)
    # t1 = nltk.UnigramTagger(t1Data, backoff=t0)
    # input = open('t2.pkl', 'rb')
    # t2Data = load(input)
    # t2 = nltk.BigramTagger(t2Data, backoff=t1)
    for i in range (len(text)):
        text[i] = nltk.pos_tag(text[i])
        # text[i] = t2.tag(text[i])
    return text

def instantiationText(text):
    for i in range (len(text)):
        for j in range(len(text[i])):
            text[i][j] = token(text[i][j][0], text[i][j][1], abrDict[text[i][j][1]])
    return(text)

def addRelation(pointingObj, pointing,type,strength):
    if strength > pointingObj.getStrength():
        pointingObj.setPointer(pointing)
        pointingObj.setPointerWord(pointing.word)
        pointingObj.setRelationshipType(type)
        pointingObj.setStrength(strength)
    else:
        return False

def ensuingAdjNoun(sentance):
    for i in range(len(sentance)):
        if isAdj(sentance[i]):
            j = i + 1
            flag = False
            while j > i and flag == False and j < len(sentance):
                if isNoun(sentance[j]):
                    if j == i + 1:
                        addRelation(sentance[i],sentance[j],'adjective to noun',10)
                        flag = True
                    else:
                        flag2 = True
                        for z in range(i,j):
                            if not(isAdj(sentance[z])):
                                flag2 = False
                        if flag2 == True:
                            addRelation(sentance[i],sentance[j],'adjective to noun',10)
                        elif flag2 == False:
                            addRelation(sentance[i],sentance[j],'adjective to noun',5)
                            flag = True
                    j = j + 1
                else:
                    j = j + 1
                    
    return sentance

def verbAdverb(sentance):
    for i in range(len(sentance)):
        flag = False
        if isAdverb(sentance[i]):
            if i+1 < len(sentance):
                if isVerb(sentance[i+1]):
                    addRelation(sentance[i],sentance[i+1],'adverb to verb',10)
                    flag = True
            if i-1 >= 0:
                if isVerb(sentance[i-1]):
                    addRelation(sentance[i],sentance[i-1],'adverb to verb',10)
                    flag = True
            j = i-1
            k = i+1
            while (j >= 0 or k < len(sentance)) and flag == False:
                if j >= 0 and flag == False:
                    if isVerb(sentance[j]):
                        addRelation(sentance[i],sentance[j],'adverb to verb',5)
                        flag = True
                    else:
                        j = j - 1
                if k < len(sentance):
                    if isVerb(sentance[k]):
                        addRelation(sentance[i],sentance[k],'adverb to verb',5)
                        flag = True
                    else:
                        k = k + 1
    return sentance

def nounVerbAdjective(sentance):
    for i in range(2,len(sentance)):
        if (isAdj(sentance[i]) and isVerb(sentance[i-1]) and isNoun(sentance[i-2])):
            addRelation(sentance[i],sentance[i-2],'adjective to noun (adjective after)',8)
        elif isAdj(sentance[i]) and isAdj(sentance[i-2]) and isListConnective(sentance[i-1]):
            addRelation(sentance[i],sentance[i-2].pointer,'adjective to noun (adjective after)',6)
    return sentance

def chaining(text):
    doc = nlp(text)
    chains = doc._.coref_chains
    return chains

def findToken(index,word,text,displacment):
    print(text)
    return displacment


sourceText = """Trash covered the landscape like sprinkles do a birthday cake. He wondered if she would appreciate his toenail collection. The fox in the tophat whispered into the ear of the rabbit. Everybody should read Chaucer to improve their everyday vocabulary. She saw no irony asking me to change but wanting me to accept her for who she is. The gloves protect my feet from excess work. She says she has the ability to hear the soundtrack of your life. They improved dramatically once the lead singer left. He didn't understand why the bird wanted to ride the bicycle. The waves were crashing on the shore; it was a lovely sight. Iguanas were falling out of the trees. Everyone pretends to like wheat until you mention barley. Everything was going so well until I was accosted by a purple giraffe. Waffles are always better without fire ants and fleas. He fumbled in the darkness looking for the light switch, but when he finally found it there was someone already there. There was coal in his stocking and he was thrilled. Please wait outside of the house. He knew it was going to be a bad day when he saw mountain lions roaming the streets. She saw the brake lights, but not in time. Three years later, the coffin was still full of Jello. You have every right to be angry, but that doesn't give you the right to be mean. There are few things better in life than a slice of pie. Please put on these earmuffs because I can't you hear. Sixty-Four comes asking for bread. It dawned on her that others could make her happier, but only she could make herself happy. The pigs were insulted that they were named hamburgers. The clouds formed beautiful animals in the sky that eventually created a tornado to wreak havoc. The snow-covered path was no help in finding his way out of the back-country. Two seats were vacant. He hated that he loved what she hated about hate. As time wore on, simple dog commands turned into full paragraphs explaining why the dog couldn't do something. Bill ran from the giraffe toward the dolphin. The wooden spoon couldn't cut but left emotional scars. The wooden spoon could cut but left emotional scars. I covered my friend in baby oil. It's never comforting to know that your fate depends on something as unpredictable as the popping of corn. So long and thanks for the fish. Let me help you with your baggage. He loved eating his bananas in hot dog buns. When transplanting seedlings, candied teapots will make the task easier. He enjoys practicing his ballet in the bathroom. Edith could decide if she should paint her teeth or brush her nails. Her daily goal was to improve on yesterday. In hopes of finding out the truth, he entered the one-room library. The river stole the gods. Their argument could be heard across the parking lot. 42.7 is a nice number. Her bag is red. The apple was green. I saw the big elephant quickly drinking from the lake. Hal played his harmonica yesterday. This is a good boy band. Ethan sat on the hill and he enjoyed it. Rodger wondered why he felt so tired. The tiger looked proud sitting on the hill, he was very happy to be up there."""

para = prepareText(text2,False)

chains = chaining(textForChaining) 
for i in range(len(chains)):
    print(i)

for sentance in para:
    combineNouns(sentance,True)
    ensuingAdjNoun(sentance)
    nounVerbAdjective(sentance)
    verbAdverb(sentance)
    seeProgress(sentance,False)
