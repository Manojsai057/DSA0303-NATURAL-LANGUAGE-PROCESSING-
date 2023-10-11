import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

sentence = "The quick brown fox jumps over the lazy dog."

tokens = nltk.word_tokenize(sentence)

pos_tags = nltk.pos_tag(tokens)

grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)

tree = cp.parse(pos_tags)

tree.draw()
