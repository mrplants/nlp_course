import spacy

# Load the installed model
nlp = spacy.load('en_core_web_md')

# Print the number of unique tokens in the vocabulary
print(len(nlp.vocab))
