from nltk import ngrams
from collections import Counter
import math

class NGram(object):
    def __init__(self, corpus, vocab):
        self.vocab = vocab
        self.corpus = []
        for w in corpus:
            self.corpus.append(vocab.stoi[w])
        self.size = len(self.corpus)
        self.ngram = {
            1: Counter(self.corpus),
            2: Counter(ngrams(self.corpus, 2)),
            3: Counter(ngrams(self.corpus, 3)),
            4: Counter(ngrams(self.corpus, 4)),
            5: Counter(ngrams(self.corpus, 5))
        }
        self.vocab_size = len(self.ngram) - 2

    def get_MLE_probs(self, word, history=None):
        if history:
            try:
                if len(history) == 1:
                    result = self.ngram[len(history) + 1][tuple(history + [word])] / \
                             self.ngram[len(history)][history[0]]
                else:
                    result = self.ngram[len(history) + 1][tuple(history + [word])] / \
                             self.ngram[len(history)][tuple(history)]
            except ZeroDivisionError:
                result = 0
        else:
            result = self.ngram[1][word] / self.size
        return result


if __name__ == '__main__':
    corpus = "My girl is learning that a girl is actually a boy".split()
    my_ngram = NGram(corpus)
    print(my_ngram.get_MLE_probs('girl'))
    history = "a".split()
    print(my_ngram.get_MLE_probs('girl', history))
