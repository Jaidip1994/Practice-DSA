from collections import Counter
import string


def cleancharacter(phrase):
    return [elem for elem in phrase.lower() if elem in string.ascii_lowercase]


def pallindrome_checker(phrase):
    final_str_freq = Counter(cleancharacter(phrase))
    return sum([elem % 2 for elem in final_str_freq.values()]) <= 1


def main():
    str_c = "Tact coa"
    print(pallindrome_checker(str_c))


if __name__ == '__main__':
    main()
