import nltk
nltk.download('punkt')

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

text = "Stemming is the process of reducing words to their base or root form"

words = nltk.word_tokenize(text)

stemmed_words = [stemmer.stem(word) for word in words]

stemmed_text = ' '.join(stemmed_words)

print("Original Text: ", text)
print("Stemmed Text: ", stemmed_text)
