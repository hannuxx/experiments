import sys, getopt

def usage():
    print('Usage: prime.py <lower-bound> <upper-bound>')
    sys.exit()

def main(argv):
    s1=""
    s2=""
    x=0
    if len(sys.argv) >= 2:
        s1 = argv[0]
        s2 = argv[1]
    else:
        usage()
    print(f'Range {s1}-{s2}')
    i1 = int(s1)
    i2 = int(s2)
    px = []
    for n in range(i1, i2):
        if n <= 1:
            continue
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            px.append(n)

    print(px)

if __name__ == "__main__":
    main(sys.argv[1:])

