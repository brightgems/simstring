from .base import BaseFeatureExtractor, DEFAULT_NGRAM_LENGTH, DEFAULT_INCLUDE_MARKS


class WordNgramFeatureExtractor(BaseFeatureExtractor):
    def __init__(self, n=DEFAULT_NGRAM_LENGTH, splitter=" ", be=DEFAULT_INCLUDE_MARKS):
        self.n = n
        self.splitter = splitter
        self.be = be

    def features(self, text):
        # Split text by white space.
        # If you want to extract words from text in more complicated way or using your favorite library like NLTK, please implement in your own.
        words = text.split(self.splitter)
        return self._words_ngram(words, self.n, self.be)
