def compare(text1, text2):
    from app.comparing_tools import Text

    (text1, text2) = (Text(text1), Text(text2))

    if text1.compare_by_theme_with(text2):
        return {'percent': 0, 'text1': [], 'text2': []}

    return {
        'percent': text1.compare_with(text2),

        'text1': [{'offset': sent.offset, 'length': sent.length}
                  for sent in text1.sentences if sent.checked],

        'text2': [{'offset': sent.offset, 'length': sent.length}
                  for sent in text2.sentences if sent.checked]
    }


if __name__ == '__main__':
    import sys
    texts = []
    for arg in sys.argv[1:]:
        texts.append(open(arg).read())
    print(compare(texts[0], texts[1]))
