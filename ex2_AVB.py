import nltk
from nltk.tokenize import word_tokenize
from nltk import bigrams
from nltk.corpus import wordnet

file = open('cleaned.txt')
raw = file.read()

tokens = nltk.word_tokenize(raw)

#unigrams
tokens = [t.lower() for t in tokens if len(t) > 1]


#bigrams
bi = bigrams(tokens)

#A)
#count word frequencys
fdist = nltk.FreqDist(tokens)
fdistbi = nltk.FreqDist(bi)

#get top 20 unigrams
unigrams = fdist.most_common(20)
#get top 20 bigrams
bigrams = fdistbi.most_common(20)

#place these into sets as per Q1 A)
unigrams = set(unigrams)
bigrams = set(bigrams)

#TODO: finish b 
#B)
#get antynoms and synonyms for unigrams
lemma = nltk.WordNetLemmatizer()
sset = {}
aset = {}
synlist = []
aynlist = []
for w in unigrams:
    syn = wordnet.synsets(w[0])
    for s in syn:
        for l in s.lemmas():
            synlist.append(l.name())

            if l.antonyms():
                aynlist.append(l.antonyms()[0].name())
                
    sset[w[0]] = synlist
    aset[w[0]] = aynlist

    synlist = []
    aynlist = []

#print syns and ants

print("Synonyms: ", sset)
print("Antonyms: ", aset)



