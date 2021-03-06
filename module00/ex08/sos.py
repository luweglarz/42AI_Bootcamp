import sys

morse_conv = { 
    'A' : '.-',     'O' : '---',    '0' : '-----',
    'B' : '-...',   'P' : '.--.',   '1' : '.----', 
    'C' : '-.-.',   'Q' : '--.-',   '2' : '..---', 
    'D' : '-..',    'R' : '.-.',    '3' : '...--', 
    'E' : '.',      'S' : '...',    '4' : '....-', 
    'F' : '..-.',   'T' : '-',      '5' : '.....', 
    'G' : '--.',    'U' : '..-',    '6' : '-....', 
    'H' : '....',   'V' : '...-',   '7' : '--...', 
    'I' : '..',     'W' : '.--',    '8' : '---..', 
    'J' : '.---',   'X' : '-..-',   '9' : '----.', 
    'K' : '-.-',    'Y' : '-.--',
    'L' : '.-..',   'Z' : '--..',
    'M' : '--',
    'N' : '-.',
}

if len(sys.argv) >= 2:
    morse = ''
    itera = 1
    while itera < len(sys.argv):
        for i in sys.argv[itera]:
            i = i.upper()
            if i == ' ':
                morse += '/'
            for j in morse_conv:
                if i == j:
                    morse += morse_conv[i]
                    morse += ' '
        morse += '/'
        itera += 1
    print(morse)