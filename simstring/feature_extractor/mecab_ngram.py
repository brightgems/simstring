import MeCab
from collections import namedtuple
from .base import BaseFeatureExtractor, DEFAULT_NGRAM_LENGTH, DEFAULT_INCLUDE_MARKS


class MecabNgramFeatureExtractor(BaseFeatureExtractor):
    def __init__(self, n=DEFAULT_NGRAM_LENGTH, be=DEFAULT_INCLUDE_MARKS, user_dic_path='', sys_dic_path=''):
        self.n = n
        self.be = be
        self.mecab = MecabTokenizer(user_dic_path, sys_dic_path)

    def features(self, text):
        words = [x.surface() for x in self.mecab.tokenize(text)]
        return self._words_ngram(words, self.n, self.be)

class Token:
    def __init__(self, surface, feature):
        token = namedtuple('Token', 'surface, pos, pos_detail1, pos_detail2, pos_detail3, infl_type, infl_form, base_form, reading, phonetic')
        self.token = token(surface, *feature)

    def baseform_or_surface(self):
        return self.token.base_form if self.token.base_form != '*' else self.token.surface

    def pos(self):
        return self.token.pos

    def pos_detail1(self):
        return self.token.pos_detail1

    def surface(self):
        return self.token.surface

class MecabTokenizer:
    def __init__(self, user_dic_path='', sys_dic_path=''):
        option = ''
        if user_dic_path:
            option += ' -d {0}'.format(user_dic_path)
        if sys_dic_path:
            option += ' -u {0}'.format(sys_dic_path)
        self._tagger = MeCab.Tagger(option)

    def tokenize(self, text):
        self._tagger.parse('')
        chunks = self._tagger.parse(text.rstrip()).splitlines()[:-1]  # Skip EOS

        tokens = []
        for chunk in chunks:
            if chunk == '':
                continue
            surface, feature = chunk.split('\t')
            feature = feature.split(',')
            if len(feature) <= 7:  # 読みがない
                feature.append('')
            if len(feature) <= 8:  # 発音がない
                feature.append('')
            tokens.append(Token(surface, feature))
        return tokens
