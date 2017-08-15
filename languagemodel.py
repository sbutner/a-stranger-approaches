import abc
import spacy
from collections import Counter

def calculate_entropy(tuples, frequency, base):
    eta = 0
    for t in tuples:
        eta -= frequency[t] * log(frequency[t])
    return eta
    #negative sum of P(x_i)*log(P(x_i))

class BaseLanguageModel(object):
    __metaclass__ = abc.ABCMeta

    


    @abc.abstractmethod
    def get_entropy(self):
        """Method should accept raw text input and return Shannon entropy
        of the input w.r.t. the language model"""

    @abc.abstractmethod
    def generate_text(self):
        """Method should return raw text output"""

    @abc.abstractmethod
    def update(self):
        """Method should alter the language model's state as appropriate"""


class HiddenMarkovLM(BaseLanguageModel):
    """Markov Chain based language model

    Attributes

    Methods

    """
    
    def __init__(self, corpus):
        self._l = 0
        self._c = Counter()
        self.update(corpus)
        
    def update(self, text):
        while n < 4:
            for ngram in self.compose_ngrams(text, n):
                _c[ngram] += 1
            n += 1
            
    @staticmethod
    def compose_ngrams(self,doc,ngram):
        i = 0
        out = []
        length = len(doc)
        for sentence in doc:
            if len(sentence) < 1:
                pass
            while i < (len(sentence) - ngram - 2):
                ngrm = (sentence[i:(i+2)].text,sentence[i+3].text)
                out.append(ngrm)
                i += 1
        return out
