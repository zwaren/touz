def compare(texts):
    from pymystem3 import Mystem
    m = Mystem()
    return m.analyze(texts[0])

if __name__ == '__main__':
    import sys
    texts = []
    for arg in sys.argv[1:]:
        texts.append(open(arg).read())
    print(compare(texts))
