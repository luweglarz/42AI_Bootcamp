import sys

if len(sys.argv) > 1:
    rev = sys.argv[1][::-1] + " "
    i = 2
    while i < len(sys.argv):
        rev = rev + str(sys.argv[i])[::-1]
        rev = rev + " "
        i += 1
    rev = rev.swapcase()
    print(rev)
