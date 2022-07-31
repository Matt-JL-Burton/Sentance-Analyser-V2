def change_letter(text, letter, index):
    return text[:index] + letter + text[index+1:]

def decimalPlaceRemoving(text):
    indices = [index for index in range(len(text)) if text.startswith('.',index)]
    for i in range(len(indices)):
        if indices[i] != 0 and indices[i] != len(text)-1:
            if text[indices[i]-1].isdigit() and text[indices[i]+1].isdigit():
                text = change_letter(text, '@', indices[i])
    return text

def decimalPlaceAdding(text):
    indices = [index for index in range(len(text)) if text.startswith('@',index)]
    for i in range(len(indices)):
        if indices[i] != 0 and indices[i] != len(text)-1:
            if text[indices[i]-1].isdigit() and text[indices[i]+1].isdigit():
                text = change_letter(text, '.', indices[i])
    return text

def printrelations(sentance):
    for i in range(len(sentance)):
        if sentance[i].pointer != None or sentance[i].coRefNum != None:
            print(vars(sentance[i]))

def seeProgress(sentance, flag):
    if flag:
        print("--------------New Sentance--------------")
        print(getSentanceENG(sentance))
        print(getSentanceType(sentance))
        print("Sentance relations:")
        printrelations(sentance)
        print()

def getSentanceENG(sentance):
    sentanceList = []
    for i in range(len(sentance)):
        if sentance[i] != None:
            sentanceList.append(sentance[i].word)
    return(sentanceList)

def getSentanceType(sentance):
    sentanceList = []
    for i in range(len(sentance)):
        if sentance[i] != None:
            sentanceList.append(sentance[i].typeComplex)
    return(sentanceList)

def isListConnective(token):
    if token.word == ',' or token.word == 'and' or token.word == 'or':
        return True
    else: 
        return False

abrDict = {
"CC":"Conjunction",
"CD":"Number", 
"DT":"Determiner",
"EX":"existential there",
"IN":"preposition",
"JJ":"adjective",
"JJR":"adjective (comparative)",
"JJS":"adjective (superlative)",
"LS":"List item marker",
"MD":"modal auxillary",
"NN":"noun",
"NNP":"noun (proper)",
"NNPS":"noun (proper, plural)",
"NNS":"noun (plural)",
"PDT":"pre-determiner",
"POS":"genative case marker ('s - possesional)",
"PRP":"personal pronoun",
"PRP$":"possesive personal pronoun",
"RB":"adverb",
"RBR":"adverb (comparitve)",
"RBS":"adverb (superlative)",
"RP":"particle",
"TO":"to - as preposition to infinitve marker e.g. to see, to go",
"UH":"interjection",
"VB":"verb",
"VBD":"verb (past tense)",
"VBG":"verb (present participle - ing words e.g. walking) ",
"VBN":"verb (past participle)",
"VBP":"verb present tense not 3rd person singular (not he/she)",
"VBZ":"verb present tesne 3rd person singular (only he/she etc)",
"WDT":"determiner (WH)~ that, what, which etc",
"WP":"pronoun (WH)~ that, what, which etc",
"WRB":"adverb (WH)~ that, what, which etc",
"$":"dollar",
"'":"closing quotation mark",
"``": "opening quotation mark",
"(":"opening parenthesis",
")": "closing parenthesis",
",":"comma",
"--":"dash",
".":"sentence terminator",
":":"colon or ellipsis",
"SYM":"symbol",
"WP$": "WH-pronoun, possessive",
"<Null Marker>":"<Null Marker>", # This is to show where the 2nd half of a composite noun was so as to allow for easier corefernital analysis
}

text2 = """
Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say
that they were perfectly normal, thank you very much. They were the last
people you'd expect to be involved in anything strange or mysterious,
because they just didn't hold with such nonsense.

Mr. Dursley was the director of a firm called Grunnings, which made
drills. He was a big, beefy man with hardly any neck, although he did
have a very large mustache. Mrs. Dursley was thin and blonde and had
nearly twice the usual amount of neck, which came in very useful as she
spent so much of her time craning over garden fences, spying on the
neighbors. The Dursleys had a small son called Dudley and in their
opinion there was no finer boy anywhere.

The Dursleys had everything they wanted, but they also had a secret, and
their greatest fear was that somebody would discover it. They didn't
think they could bear it if anyone found out about the Potters. Mrs.
Potter was Mrs. Dursley's sister, but they hadn't met for several years;
in fact, Mrs. Dursley pretended she didn't have a sister, because her
sister and her good-for-nothing husband were as unDursleyish as it was
possible to be. The Dursleys shuddered to think what the neighbors would
say if the Potters arrived in the street. The Dursleys knew that the
Potters had a small son, too, but they had never even seen him. This boy
was another good reason for keeping the Potters away; they didn't want
Dudley mixing with a child like that.
"""