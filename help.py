import nltk
from nltk.corpus import stopwords
from main import combineNouns, prepareText
from general import seeProgress
from sentanceAnalysis import token


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
}

sourceText = """His confidence would have been admirable if it wasn't for his stupidity. The hummingbird's wings blurred while it eagerly sipped the sugar water from the feeder. He's in a boy band which doesn't make much sense for a snake. The overpass went under the highway and into a secret world. She moved forward only because she trusted that the ending she now was going through must be followed by a new beginning. Trash covered the landscape like sprinkles do a birthday cake. He wondered if she would appreciate his toenail collection. The fox in the tophat whispered into the ear of the rabbit. Everybody should read Chaucer to improve their everyday vocabulary. She saw no irony asking me to change but wanting me to accept her for who she is. The gloves protect my feet from excess work. She says she has the ability to hear the soundtrack of your life. They improved dramatically once the lead singer left. He didn't understand why the bird wanted to ride the bicycle. The waves were crashing on the shore; it was a lovely sight. Iguanas were falling out of the trees. Everyone pretends to like wheat until you mention barley. Everything was going so well until I was accosted by a purple giraffe. Waffles are always better without fire ants and fleas. He fumbled in the darkness looking for the light switch, but when he finally found it there was someone already there. There was coal in his stocking and he was thrilled. Please wait outside of the house. He knew it was going to be a bad day when he saw mountain lions roaming the streets. She saw the brake lights, but not in time. Three years later, the coffin was still full of Jello. You have every right to be angry, but that doesn't give you the right to be mean. There are few things better in life than a slice of pie. Please put on these earmuffs because I can't you hear. Sixty-Four comes asking for bread. It dawned on her that others could make her happier, but only she could make herself happy. The pigs were insulted that they were named hamburgers. The clouds formed beautiful animals in the sky that eventually created a tornado to wreak havoc. The snow-covered path was no help in finding his way out of the back-country. Two seats were vacant. He hated that he loved what she hated about hate. As time wore on, simple dog commands turned into full paragraphs explaining why the dog couldn’t do something. Bill ran from the giraffe toward the dolphin. The wooden spoon couldn’t cut but left emotional scars. I covered my friend in baby oil. It's never comforting to know that your fate depends on something as unpredictable as the popping of corn. So long and thanks for the fish. Let me help you with your baggage. He loved eating his bananas in hot dog buns. When transplanting seedlings, candied teapots will make the task easier. He enjoys practicing his ballet in the bathroom. Edith could decide if she should paint her teeth or brush her nails. Her daily goal was to improve on yesterday. In hopes of finding out the truth, he entered the one-room library. The river stole the gods. Their argument could be heard across the parking lot."""

# Known issues
# mis labelling of items, e.g. elephant as adjective
# "everything i heard today was really really interesting"
