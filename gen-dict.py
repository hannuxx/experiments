#!/usr/bin/python3

import sys, getopt

def help():
    print('gen-dict.py --input file --lang <language> --pattern <pattern>')
    sys.exit()

def main(argv):
    ifile = ''
    lang = 'fin'
    pattern = ''

    try:
        opts, args = getopt.getopt(argv, 'hi:l:p:' ,["help", "input=", "lang=","pattern="])
    except getopt.GetoptError:
        print("WTF!")
        help()

    for opt, arg in opts:
        print('opt: ', opt, ' arg:', arg)
        if opt in ("-h", "--help"):
            help()
        elif opt in ("-i", "--input"):
            ifile = arg
        elif opt in ("-l", "--lang"):
            lang = arg
        elif opt in ("-p", "--pattern"):
            pattern = arg
    print('Input file is ', ifile)
    print('Language is ', lang)
    print('Pattern is ', pattern)

if __name__ == "__main__":
    main(sys.argv[1:])

