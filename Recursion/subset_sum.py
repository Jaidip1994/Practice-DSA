def subsetSums(arrlist):
    arrlist.sort()
    n = len(arrlist)
    for i in range(1 << n):
        temp_val = 0
        for j in range(n):
            if (i & (1 << j)) > 0:
                temp_val += arrlist[j]
        print(temp_val)


def main():
    # subsetSums([3, 1, 2])
    # subsetSums([2, 3])
    subsetSums([5, 2, 1])


if __name__ == '__main__':
    main()
