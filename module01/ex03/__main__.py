from generator import generator

def main():
    text ="Z A C D B E F"
    print("Test with ordered option:")
    print("____________________________")
    for i in generator(text, " ", "ordered"):
        print(i)

    text ="Le mot unique est le mot unique"
    print("Test with ordered unique:")
    print("____________________________")
    for i in generator(text, " ", "unique"):
        print(i)

    text ="Je shuffle ce texte pour la science"
    print("Test with ordered shuffle:")
    print("____________________________")
    for i in generator(text, " ", "shuffle"):
        print(i)

if __name__ == "__main__":
    main()