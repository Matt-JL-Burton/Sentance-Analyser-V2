import coreferee
import spacy
nlp = spacy.load('en_core_web_lg')
nlp.add_pipe('coreferee')