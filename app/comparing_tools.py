import re

from pymystem3 import Mystem

mystem = Mystem()


class Text:
    def __init__(self, text):
        self.raw = text
        self.sentences = [Sentence(text.find(sent), sent)
                          for sent in re.split(r'[.!?]\s', text)]

    def compare_by_theme_with(self, other):
        return 1

    def compare_with(self, other):
        similarity = 0
        for sentence1 in self.sentences:
            for sentence2 in other.sentences:
                if not sentence2.checked:
                    result = sentence1.compare_with(sentence2)
                    if result > 0.9:
                        sentence1.checked = True
                        sentence2.checked = True
                    similarity += result
            
        return similarity / len(self.sentences)

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
        self.stems = self.get_stems(sentence)
        self.checked = False

    def get_stems(self, sentence):
        stems = []
        for stem in mystem.analyze(sentence):
            if 'analysis' in stem:
                stem['gr'] = stem['analysis'][0]['gr']
                stem['lex'] = stem['analysis'][0]['lex']
                del stem['analysis']
                stem['gr'] = stem['gr'].replace('=', ',')
                for substr in re.findall(r'(\(.*\|+.*\))+?', stem['gr']):
                    stem['gr'] = stem['gr'].replace(
                        substr, substr.split('|')[0][1:])
                stem['gr'] = stem['gr'].split(',')
                stems.append(stem)
        return stems

    def compare_with(self, other):
        similarity = 0
        for i in range(len(self.stems)):
            if self.stems[i]['gr'][0] == other.stems[i]['gr'][0]:
                similarity += .5
                if self.stems[i]['lex'] == other.stems[i]['lex']:
                    similarity += .5
        return similarity / len(self.stems)

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


if __name__ == "__main__":
    x = Text('Значимость этих проблем настолько очевидна, что сложившаяся структура организации играет важную роль в формировании систем массового участия')
    y = Text("Значимость этих проблем настолько понятна, что получившаяся модель организации играет важную роль в формировании систем массового участия")
    print(x.compare_with(y))
    print("x: {0}\ny: {1}".format(x, y))
