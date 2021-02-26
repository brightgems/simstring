from .base import BaseFeatureExtractor, DEFAULT_NGRAM_LENGTH, DEFAULT_INCLUDE_MARKS


class CharacterNgramFeatureExtractor(BaseFeatureExtractor):
    def __init__(self,  n=DEFAULT_NGRAM_LENGTH, be=DEFAULT_INCLUDE_MARKS):
        self.n = n
        self.be = be

    def features(self, string):
        return self._each_cons(string, self.n, self.be)
