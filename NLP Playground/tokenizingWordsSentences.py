from nltk.tokenize import sent_tokenize, word_tokenize

EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

#print(sent_tokenize(EXAMPLE_TEXT))
#print(word_tokenize(EXAMPLE_TEXT))

print(sent_tokenize(EXAMPLE_TEXT)[2])

for i in word_tokenize(EXAMPLE_TEXT):
    print(i)
