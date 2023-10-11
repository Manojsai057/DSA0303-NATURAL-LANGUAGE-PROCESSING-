import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = "Part-of-speech tagging is essential in natural language processing."

words = word_tokenize(text)

pos_tags = pos_tag(words)

print("Tokenized Words:")
print(words)

print("\nPOS Tags:")
print(pos_tags)
