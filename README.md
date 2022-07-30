# Sentance-Analyser
A work experience project that aims to try and understand the purpose of different words in a sentence

- **Useful documentation:**
	- NLTK : https://www.nltk.org/
	- NLTK Book : https://www.nltk.org/book/
	- Coreference Resolution : https://towardsdatascience.com/intro-to-coreference-resolution-in-nlp-19788a75adee
<br>
<br>

_**Current Issues:**_
- The current tagger could be imporved
    - This could be done by using a personally curated tagger as seen in, by combining taggers and training test data. I can do this however I don't think the results would be better than using the current imperfect tagger

- Trying to pair pronouns to proper nouns and nouns. E.g. He - Jerrald, They - Tigers etc (but in conext it is obviosubl more complex)
    - There are two main types of co-references between pronouns and nouns, anaphora (after) and cataphora (before), where the before/after refers to the positon of pronoun (or equivilent) in relation to the [proper] noun
    - pleontasitc 'it', for example "It was raining heavily" - the refers to nothing but is still requird.
- Need t0 intergrate co-referentails
