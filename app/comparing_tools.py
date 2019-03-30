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

    def get_json(self):
        return [sent.get_json() for sent in self.sentences]

    def __repr__(self):
        return str(self.sentences)

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

    def get_json(self):
        return {
            'offset': self.offset,
            'length': self.length,
            'checked': self.checked,
            'stems': self.stems
        }

    def __repr__(self):
        return str(self.get_json())

    def __str__(self):
        return str(self.get_json())
