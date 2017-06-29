import spacy
from collections import Counter

def calculateEntropy():
    #get the frequencies of each label, divide by total length to calculate obs p
    #negative sum of P(x_i)*log(P(x_i)) (conditional entropy is -sum p(x_i,y_j)*log(p(x_i,y_j)/p(y_j))

class LanguageModel():
    def __init__(self, corpus, ngram=7):
        corpus = self.corpus
        ngram = self.ngram
    def gatherFrequencies(tuples):
        count = Counter()
        for tup in tuples:
            count[tup] += 1
        return count
    def ngramCorpus(corpus, ngram):
        i = 0
        out = []
        
        for sentence in corpus:
            if len(sentence) < 1:
                pass
            while i < (len(sentence) - ngram - 2):
                ngrm = (sentence[i:(i+2)].text,sentence[i+3].text)
                i += 1
                out.append(ngrm)
        return out
