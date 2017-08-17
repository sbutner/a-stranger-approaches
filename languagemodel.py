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

    @abc.abstractmethod
    def get_compression(self):
        """Method should return a compression factor of the input"""


class HiddenMarkovLM(BaseLanguageModel):
    """Markov Chain based language model

    Attributes

    Methods

    """
    
    def __init__(self, corpus):
        self._l = 0
        self._emissions = Counter()
        self._transitions = Counter()
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

class TextStorage(object):
    """Storage for string literals
    TODO: bigrams should be pushed down into the markov models
    as tuples of unigram indices.
    the static methods should come out from the class
    oh java has addled my brain
    """
    unigrams = list()
    _u_idx = 0
    bigrams = list()
    _b_idx = 0
    _uni = dict()
    _bi = dict()

    @staticmethod    
    def add_unigram(unigram):
        TextStorage.unigrams.append(unigram)
        TextStorage._u_idx += 1
    @staticmethod
    def add_bigram(bigram):
        TextStorage.bigrams.append(bigram)
        TextStorage._b_idx
    @staticmethod
    def get_index(ngram):
        """returns the index for some slice of text
        assigns the slice to a unique index if missing"""
        
        if len(ngram) == 2:
            return TextStorage._get_b_idx(ngram)
        elif len(ngram) == 1:
            return TextStorage._get_u_idx(ngram)

    @staticmethod
    def _get_b_idx(ngram):
        if ngram in TextStorage._bi:
            return TextStorage._bi[ngram]
        else:
            TextStorage._bi[ngram] = TextStorage._b_idx
            TextStorage._b_idx += 1
            TextStorage._get_b_idx(ngram)

    @staticmethod
    def _get_u_idx(ngram):
        if ngram in TextStorage._uni:
            return TextStorage._uni[ngram]
        else:
            TextStorage._uni[ngram] = TextStorage._u_idx
            TextStorage._u_idx += 1
            TextStorage._get_u_idx(ngram)

        
    

class LocalHMModel(object):
    """Total vocabulary of the language model
    contains Ngram objects
    """

    def __init__(self):
        self._vocabulary = dict()
        self._total_symb = 0
        self._total_count = 0
        
    def get_symbol(self, text):
        _ = TextStorage.get_index(text)
        if _ in self._vocabulary:
            self._vocabulary[_].update()
            self._total_count += 1
        else:
            self._vocabulary[_] = Ngram(_)
            self._total_symb += 1
            self._total_count += 1
        return self._vocabulary[_]
    
    def get_symbol_emission(self, ngram):
        if ngram in self._vocabulary:
            return self._vocabulary[ngram].frequency / self._total_count
        else:
            self.add_symbol(ngram)
            self._vocabulary[ngram].frequency / self._total_count
    def draw_symbol(self, condition):
        if condition == EOS:
            probs = 0
            roll = random.random()
            for gram in self._vocabulary:
                if probs <= roll:
                    probs += self.get_symbol_emission(gram)
        else:
            probs = 0
            roll = random.random()
            for gram in self._vocabulary:
                if probs <= roll:
                    probs += self.get_symbol_emission(gram)

class Ngram(object):
    """Node in markov chain
    belongs to a LocalHMModel
    Unlikely to access directly
    """

    def __init__(self, index):
        self.index = index
        self.transitions = Counter()
        self.frequency = 1
    def add_transition(self, gram):
        self.transitions[gram] += 1
    def update(self):
        self.frequency += 1
    def get_transition_probability(self, next_gram):
        return self.transitions[next_gram] / self.frequency
    def text(self):
        return TextStorage.get_text(self.index)
    def draw_transition(self):
        next_probs = 0
        roll = random.random()
        for gram in self.transitions:
            if next_probs <= roll:
                next_probs += self.get_transition_probability(gram)
        
        
