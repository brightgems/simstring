
# Length of n-grams in simstring DBs
DEFAULT_NGRAM_LENGTH = 2

# Whether to include marks for begins and ends of strings
DEFAULT_INCLUDE_MARKS = True


class BaseFeatureExtractor:

    def features(self, _string):
        raise NotImplementedError()

    def _each_cons(self, s, n, be):
        mark = " "
        src = ''
        if be:
            # affix begin/end marks
            src = mark + s + mark
        elif len(s) < n:
            # pad strings shorter than n
            src = s
            for i in range(n - len(s)):
                src += mark
        else:
            src = s
        return [src[i:i+n] for i in range(len(src)-n+1)]

    def _words_ngram(self, words, n=DEFAULT_NGRAM_LENGTH, be=DEFAULT_INCLUDE_MARKS):
        """
        implementation mirroring ngrams() in ngram.h in simstring-1.0
        distribution.
        """
        # count n-grams
        out = set()
        stat = {}
        for ngram in self._each_cons(words, n, be):
            stat[ngram] = stat.get(ngram, 0) + 1

        # convert into a set
        for ngram, count in list(stat.items()):
            out.add(ngram)
            # add ngram affixed with number if it appears more than once
            for i in range(1, count):
                out.add(ngram + str(i + 1))

        return out
