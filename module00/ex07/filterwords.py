import sys
import string

if len(sys.argv) != 3:
    print("ERROR")
else:
    strlist = sys.argv[1].split(" ")
    filtred = []
    for i in strlist:
        if len(i) > int(sys.argv[2]):
            filtred.append(i.translate(str.maketrans('', '', string.punctuation)))
    print(filtred)
    