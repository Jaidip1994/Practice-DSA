# Finding the first repeated character using count
def first_repeated_char(pstr):
    checker = 0
    for idx, elem in enumerate(pstr):
        bpos = ord(elem) - ord('a')
        if (checker & (1 << bpos)) > 0:
            return idx
        checker |= 1 << bpos
    print(bin(checker))
    return -1


def main():
    fstr = 'abcdz'
    idx = first_repeated_char(fstr)
    if idx != -1:
        print(f'Found first repeating at {idx}')
    else:
        print('No repeating character')


if __name__ == '__main__':
    main()
