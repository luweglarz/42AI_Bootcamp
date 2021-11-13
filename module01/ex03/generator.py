from random import shuffle

def generator(text, sep=" ", option=None):
    str = text.split(sep)
    if option == None:
        for i in str:
            yield i
    if option == "ordered":
        str.sort()
        for i in str:
            yield i
    elif option == "unique":
        unique = []
        [unique.append(word) for word in str if word not in unique]
        for i in unique:
            yield i
    elif option == "shuffle":
        shuffle(str)
        for i in str:
            yield i