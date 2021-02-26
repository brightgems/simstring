import jieba
from collections import namedtuple
from .base import BaseFeatureExtractor, DEFAULT_NGRAM_LENGTH, DEFAULT_INCLUDE_MARKS


class JiebaNgramFeatureExtractor(BaseFeatureExtractor):
    def __init__(self, n=DEFAULT_NGRAM_LENGTH, be=DEFAULT_INCLUDE_MARKS):
        self.n = n
        self.be = be

    def features(self, text):
        words = [x for x in jieba.cut(text) if x.strip()]
        return self._words_ngram(words, self.n, self.be)
