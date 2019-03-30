import re

from pymystem3 import Mystem

mystem = Mystem()


class Text:
    def __init__(self, text):
        self.raw = text
        self.sentences = [Sentence(text.find(sent), sent)
                          for sent in re.split(r'[.!?]\s', text)]

    def compare_by_theme_with(self, other):
        return False

    def compare_with(self, other):
        return 100

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.sentences)


class Sentence:
    def __init__(self, offset, sentence):
        self.offset = offset
        self.length = len(sentence)
        self.sentence = sentence
        self.stems = [stem for stem in mystem.analyze(sentence)
                      if 'analysis' in stem]
        self.checked = False

    def compare_with(self, other): pass

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "{{'offset': {0}, 'length': {1}, 'checked': {2}, 'stems': {3}}}" \
            .format(self.offset, self.length, self.checked, self.stems)
