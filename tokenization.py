import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

text = "Tokenization is the process of breaking text into words and sentences. It's an important step in NLP."

words = word_tokenize(text)

sentences = sent_tokenize(text)

print("Tokenized Words:")
print(words)

print("\nTokenized Sentences:")
print(sentences)
