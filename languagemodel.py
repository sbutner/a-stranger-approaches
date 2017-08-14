import spacy
from collections import Counter

def calculateEntropy(tuples, frequency, base):
    eta = 0
    for t in tuples:
        eta -= frequency[t] * log(frequency[t])
    return eta
    #negative sum of P(x_i)*log(P(x_i))

class LanguageModel(corpus, ngram, l, c):
    def __init__(self, corpus, ngram=7, l, c):
        self.corpus = corpus
        self.ngram = ngram
        self.l = 0
        while n < ngram:
            self.c += composeFrequencies(corpus, n)
            n += 1
    def composeFrequencies(self,corpus, ngram):
        c = Counter()
        for doc in corpus:
            t = ngramCorpus(doc, ngram)
            l += gatherLength(doc)
            c += gatherFrequencies(t)
        for key in c:
            c[key] = float(c[key]) / l
        return c
    def gatherFrequencies(self,tuples):
        count = Counter()
        for tup in tuples:
            count[tup] += 1
        return count
    def gatherLength(self,doc):
        length = len(doc)
        return length
    def ngramCorpus(self,doc, ngram):
        i = 0
        out = []
        length = len(doc)
        for sentence in corpus:
            if len(sentence) < 1:
                pass
            while i < (len(sentence) - ngram - 2):
                ngrm = (sentence[i:(i+2)].text,sentence[i+3].text)
                i += 1
                out.append(ngrm)
        return out
