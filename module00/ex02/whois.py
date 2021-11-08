import sys

if len(sys.argv) == 2 and sys.argv[1].isnumeric():
    if (int(sys.argv[1]) % 2 == 0):
        print("I'm even")
    else:
        print("I'm odd")
else:
    print("Error")
