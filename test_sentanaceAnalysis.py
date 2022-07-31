from cgi import test
import unittest
import nltk 
from main import splitTextSen, tokenizeText, ensuingAdjNoun, verbAdverb, nounVerbAdjective, removeStopWords, taggingText, instantiationText, prepareText, deAbreviate, preCoRefPreparation, addCoRefrenceRels
from sentanceAnalysis import token
from general import *
from nouns import combineNouns

print("\nTesting Started")

class tests(unittest.TestCase):
    
    def test_sentanceSplitting(self):
        test_Sentance1 = "I am a student! I love to code"
        self.assertEqual(splitTextSen(test_Sentance1),["I am a student!","I love to code"])
        test_Sentance2 = "Finally, the rain has stopped. The rain was making it difficult to see the fields. \n Now I can see them"
        self.assertEqual(splitTextSen(test_Sentance2),["Finally, the rain has stopped.","The rain was making it difficult to see the fields.","Now I can see them"])

    def test_tokenizing(self):
        test_Sentance1 = "Hal played his harmonica yesterday"
        self.assertEqual(tokenizeText(splitTextSen(test_Sentance1)),[["Hal","played","his","harmonica","yesterday"]])
        test_Sentance2 = "Hal played his harmonica yesterday. This upset the neighbours"
        self.assertEqual(tokenizeText(splitTextSen(test_Sentance2)),[["Hal","played","his","harmonica","yesterday", "."],['This','upset','the','neighbours']])

    def test_removeStopingWords(self):
        test_Sentance1 = "Nick likes to play football, however he is not too fond of tennis. He likes rugby more than football"
        self.assertEqual(removeStopWords(tokenizeText(splitTextSen(test_Sentance1)),True),[["Nick","likes","play","football",",","however","fond","tennis","."],["likes","rugby","football"]])

    def test_deAbbrevaite(self):
        test_sentance1 = "I don't like this code. This wasn't cool"
        self.assertEqual(deAbreviate(test_sentance1),"I do not like this code. This was not cool")
        test_sentance2 = "I don't like this code, it wasn't cool"
        self.assertEqual(deAbreviate(test_sentance2),"I do not like this code, it was not cool")
        test_sentance3 = "It isn't that he's one of best. He just might've cheated often. I'm disappointed in him for that."
        self.assertEqual(deAbreviate(test_sentance3),"It is not that he is one of best. He just might have cheated often. I am disappointed in him for that.")

    def test_taggingText(self):
        test_Sentance1 = "Hal played his harmonica yesterday"
        self.assertEqual(taggingText(tokenizeText(splitTextSen(test_Sentance1)))[0][0],("Hal","NNP"))
        self.assertEqual(taggingText(tokenizeText(splitTextSen(test_Sentance1)))[0][1],("played","VBD"))
        self.assertEqual(taggingText(tokenizeText(splitTextSen(test_Sentance1)))[0][2],("his","PRP$"))
        self.assertEqual(taggingText(tokenizeText(splitTextSen(test_Sentance1)))[0][3],("harmonica","NN"))
        # self.assertEqual(taggingText(tokenizeText(splitTextSen(test_Sentance1)))[0][4],("yesterday","JJ")) #FIXME:
        test_Sentance2 = "Hal played his harmonica yesterday. This upset the neighbours"
        self.assertEqual(taggingText(tokenizeText(splitTextSen(test_Sentance2)))[0][5],(".","."))
        self.assertEqual(taggingText(tokenizeText(splitTextSen(test_Sentance2)))[1][1],("upset","VBZ"))
        self.assertEqual(taggingText(tokenizeText(splitTextSen(test_Sentance2)))[1][3],("neighbours","NNS"))

    def test_instantiationText(self):
        test_Sentance1 = "Look up at the sky"
        self.assertEqual(instantiationText(taggingText(tokenizeText(splitTextSen(test_Sentance1))))[0][0].word,"Look")
        self.assertEqual(instantiationText(taggingText(tokenizeText(splitTextSen(test_Sentance1))))[0][1].word,"up")
        self.assertEqual(instantiationText(taggingText(tokenizeText(splitTextSen(test_Sentance1))))[0][4].typeComplex,"noun")
        test_Sentance2 = "This a great boy band. My sister loves them"
        self.assertEqual(instantiationText(taggingText(tokenizeText(splitTextSen(test_Sentance2))))[1][0].word,"My")
        self.assertEqual(instantiationText(taggingText(tokenizeText(splitTextSen(test_Sentance2))))[1][1].pointer,None)

    def test_prepareText(self):
        self.assertEqual(prepareText("I am a student! I love to code",False)[0][0].word,'I')
        self.assertEqual(prepareText("I am a student! I love to code",True)[0][0].word,'student')

    def test_combineNouns(self):
        test_Sentance1 = prepareText("I love this boy band",False)[0]
        self.assertEqual(combineNouns((test_Sentance1),True)[3].word,"boy band")
        self.assertEqual(combineNouns((test_Sentance1),True)[4].word,"<Null Marker>")
        test_Sentance2 = prepareText("Look at this mountain lion",False)[0]
        self.assertEqual(combineNouns((test_Sentance2),True)[3].word,"mountain lion")
        test_Sentance3 = prepareText("The wooden spoon couldn't cut",False)[0]
        self.assertEqual(combineNouns((test_Sentance3),True)[2].word,"spoon")

    def test_adjToNoun(self):
        test_Sentance1 = ensuingAdjNoun(prepareText("This is a really big lion",False)[0])
        self.assertEqual(test_Sentance1[4].pointerWord,"lion")
        self.assertEqual(test_Sentance1[4].relType,"adjective to noun")
        self.assertEqual(test_Sentance1[4].strength,10)
        test_Sentance2 = ensuingAdjNoun(prepareText("There is a lot of deep pain routed in his large eyes",False)[0])
        self.assertEqual(test_Sentance2[5].pointerWord,"pain")
        self.assertEqual(test_Sentance2[5].relType,"adjective to noun")
        self.assertEqual(test_Sentance2[5].strength,10)
        self.assertEqual(test_Sentance2[10].pointerWord,"eyes")
        self.assertEqual(test_Sentance2[10].relType,"adjective to noun")
        self.assertEqual(test_Sentance2[10].strength,10)
        test_Sentance3 = ensuingAdjNoun(prepareText("He has big green teeth and a small but nice smile",False)[0])
        self.assertEqual(test_Sentance3[2].pointerWord,"teeth")
        self.assertEqual(test_Sentance3[2].relType,"adjective to noun")
        self.assertEqual(test_Sentance3[2].strength,10)
        self.assertEqual(test_Sentance3[3].pointerWord,"teeth")
        self.assertEqual(test_Sentance3[3].relType,"adjective to noun")
        self.assertEqual(test_Sentance3[3].strength,10)
        self.assertEqual(test_Sentance3[7].pointerWord,"smile")
        self.assertEqual(test_Sentance3[7].relType,"adjective to noun")      
        self.assertEqual(test_Sentance3[7].strength,5)
        self.assertEqual(test_Sentance3[9].pointerWord,"smile")
        self.assertEqual(test_Sentance3[9].relType,"adjective to noun")      
        self.assertEqual(test_Sentance3[9].strength,10)
    
    def test_adverbToVerb(self):
        test_Sentance1 = verbAdverb(prepareText("I saw the big elephant quickly drinking from the lake",False)[0])
        self.assertEqual(test_Sentance1[5].pointerWord,"drinking")
        self.assertEqual(test_Sentance1[5].relType,"adverb to verb")
        self.assertEqual(test_Sentance1[5].strength,10)
        test_Sentance2 = verbAdverb(prepareText("She looked lovingly into his eyes",False)[0])
        self.assertEqual(test_Sentance2[2].pointerWord,"looked")
        self.assertEqual(test_Sentance2[2].relType,"adverb to verb")
        self.assertEqual(test_Sentance2[2].strength,10)
        test_Sentance3 = verbAdverb(prepareText("I quickly scanned the horizen",False)[0])
        self.assertEqual(test_Sentance3[1].pointerWord,"scanned")
        self.assertEqual(test_Sentance3[1].relType,"adverb to verb")
        self.assertEqual(test_Sentance3[1].strength,10)
        test_Sentance4 = verbAdverb(prepareText("I am now carefully testing all my code",False)[0])
        self.assertEqual(test_Sentance4[3].pointerWord,"testing")
        self.assertEqual(test_Sentance4[3].relType,"adverb to verb")
        self.assertEqual(test_Sentance4[3].strength,10)
        test_Sentance5 = verbAdverb(prepareText("Amy began to quickly walk across the street, before rapidly hurrying out the way of the car",False)[0])
        self.assertEqual(test_Sentance5[3].pointerWord,"walk")
        self.assertEqual(test_Sentance5[3].relType,"adverb to verb")
        self.assertEqual(test_Sentance5[3].strength,10)
        self.assertEqual(test_Sentance5[10].pointerWord,"hurrying")
        self.assertEqual(test_Sentance5[10].relType,"adverb to verb")
        self.assertEqual(test_Sentance5[10].strength,10)
        # test_Sentance6 = verbAdverb(prepareText("Hal played his harmonica yesterday",False)[0]) FIXME: - yesterday is being misidentified as a noun
        # self.assertEqual(test_Sentance6[4].pointerWord,"played")
        # self.assertEqual(test_Sentance6[4].relType,"adverb to verb")
        # self.assertEqual(test_Sentance6[4].strength,5)
        test_Sentance7 = verbAdverb(prepareText("The children ran outside",False)[0])
        self.assertEqual(test_Sentance7[3].pointerWord,None)
        test_Sentance8 = verbAdverb(prepareText("The bird is happy outside the cages",False)[0])
        self.assertEqual(test_Sentance8[4].pointerWord,None)

    def test_nounVerbAdj(self):
        test_Sentance1 = nounVerbAdjective(prepareText("The elephant was green",False)[0])
        self.assertEqual(test_Sentance1[3].pointerWord,"elephant")
        self.assertEqual(test_Sentance1[3].relType,"adjective to noun (adjective after)")
        self.assertEqual(test_Sentance1[3].strength,8)
        test_Sentance2 = nounVerbAdjective(prepareText("The elephant was green and big",False)[0])
        self.assertEqual(test_Sentance2[3].pointerWord,"elephant")
        self.assertEqual(test_Sentance2[3].relType,"adjective to noun (adjective after)")
        self.assertEqual(test_Sentance2[3].strength,8)
        self.assertEqual(test_Sentance2[5].pointerWord,"elephant")
        self.assertEqual(test_Sentance2[5].relType,"adjective to noun (adjective after)")
        self.assertEqual(test_Sentance2[5].strength,6)
        test_Sentance3 = nounVerbAdjective(prepareText("The elephant was green, big and loud",False)[0])
        self.assertEqual(test_Sentance3[3].pointerWord,"elephant")
        self.assertEqual(test_Sentance3[3].relType,"adjective to noun (adjective after)")
        self.assertEqual(test_Sentance3[3].strength,8)
        self.assertEqual(test_Sentance3[5].pointerWord,"elephant")
        self.assertEqual(test_Sentance3[5].relType,"adjective to noun (adjective after)")
        self.assertEqual(test_Sentance3[5].strength,6)
        self.assertEqual(test_Sentance3[7].pointerWord,"elephant")
        self.assertEqual(test_Sentance3[7].relType,"adjective to noun (adjective after)")
        self.assertEqual(test_Sentance3[7].strength,6)
        test_Sentance4 = nounVerbAdjective(prepareText("The elephant was a big animal",False)[0])
        self.assertFalse(test_Sentance4[4].pointerWord,"elephant")

    def test_sameSentancePronounLinking(self):
        test_Sentance1 = "Barry looked lost. He was depressed"
        test_Sentance1_Prep = prepareText(test_Sentance1,False)
        addCoRefrenceRels(preCoRefPreparation(test_Sentance1),test_Sentance1_Prep)
        self.assertEqual(test_Sentance1_Prep[0][0].coRefNum,0)
        self.assertEqual(test_Sentance1_Prep[1][0].coRefNum,0)
        self.assertEqual(test_Sentance1_Prep[1][1].coRefNum,None)
        test_Sentance2 = """Mr. Dursley was the director of a firm called
Grunnings, which made drills. He was a big, beefy
man with hardly any neck, although he did have a
very large mustache. Mrs. Dursley was thin and
blonde and had nearly twice the usual amount of
neck, which came in very useful as she spent so
much of her time craning over garden fences, spying
on the neighbors. The Dursley s had a small son
called Dudley and in their opinion there was no finer
boy anywhere."""
        test_Sentance2_Prep = prepareText(test_Sentance2,False)
        addCoRefrenceRels(preCoRefPreparation(test_Sentance2),test_Sentance2_Prep)
        self.assertEqual(test_Sentance2_Prep[0][1].coRefNum,0)
        self.assertEqual(test_Sentance2_Prep[1][0].coRefNum,0)
        self.assertEqual(test_Sentance2_Prep[1][13].coRefNum,0)
        self.assertEqual(test_Sentance2_Prep[2][1].coRefNum, 1)
        self.assertEqual(test_Sentance2_Prep[2][22].coRefNum, 1)

if __name__ == '__main__':  
    unittest.main() 