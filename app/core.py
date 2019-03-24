def compare(text1, text2):
    from pymystem3 import Mystem
    m = Mystem()
    return m.analyze(text1)


if __name__ == '__main__':
    import sys
    texts = []
    for arg in sys.argv[1:]:
        texts.append(open(arg).read())
    print(compare(texts[0], texts[1]))
