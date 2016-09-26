from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an obviously massive challenge, but there are steps to doing it that anyone can follow. The main idea, however, is that computers simply do not, and will not, ever understand words directly. Humans don't either *shocker*. In humans, memory is broken down into electrical signals in the brain, in the form of neural groups that fire in patterns. There is a lot ab"

stop_words = set(stopwords.words("english"))

words = word_tokenize(example_sentence)

filtered_sentence = [w for w in words if not w in stop_words]

##for w in words:
##    if w not in stop_words:
##        filtered_sentence.append(w)
##
##
print(filtered_sentence)
