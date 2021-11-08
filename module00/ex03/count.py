

def text_analyzer(*text):
    """
    text_analyzer.

    :param param1: the string you want to analyze
    :returns:
    the amount of [upper, lower, punctuation, space] letters in the string
    """
    if len(text) > 1:
        print("ERROR")
        return
    punc_list = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    upper = 0
    lower = 0
    punctuation = 0
    space = 0
    for i in text[0]:
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1
        if i in punc_list:
            punctuation += 1
        if i == ' ':
            space += 1

    print(upper, "upper letters")
    print(lower, "lower letters")
    print(punctuation, "punctuation letters")
    print(space, "space letters")
