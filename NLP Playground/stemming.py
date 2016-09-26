from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["train", "trainer", "training", "trained"]

##for w in example_words:
##    print(ps.stem(w))

text = "My trainer, jack, worked to train me in martial arts while we were riding on a train. He trained me good."

words = word_tokenize(text)

for w in words:
    print(ps.stem(w))
