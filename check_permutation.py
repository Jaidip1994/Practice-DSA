#  Given two strings write a method to decide if one is a substring of another
def permutation_with_nlogn(str1, str2):
    if len(str1) != len(str2):
        return False

    str1 = list(str1)
    str2 = list(str2)

    str1.sort()
    str2.sort()

    return str1 == str2


def permutation_with_count(str1, str2):
    if len(str1) != len(str2):
        return False
    count_arr = [0] * 256
    for idx in range(len(str1)):
        count_arr[ord(str1[idx])] += 1
        count_arr[ord(str2[idx])] -= 1

    for elem in count_arr:
        if elem != 0:
            return False
    return True


def main():
    print(permutation_with_nlogn("test", "ttes"))
    print(permutation_with_count("test", "toes"))


if __name__ == '__main__':
    main()
