def subsetSums(arrlist):
    arrlist.sort()
    n = len(arrlist)
    for i in range(1 << n):
        temp_val = 0
        for j in range(n):
            if (i & (1 << j)) > 0:
                temp_val += arrlist[j]
        print(temp_val)


final_arr = []


def subset_recr(idx, sum, arr):
    if idx == len(arr):
        final_arr.append(sum)
        return
    subset_recr(idx + 1, sum + arr[idx], arr)
    subset_recr(idx + 1, sum, arr)


def main():
    # subsetSums([3, 1, 2])
    # subsetSums([2, 3])
    subsetSums([5, 2, 1])
    subset_recr(0, 0, [5, 1, 2])
    final_arr.sort()
    print(final_arr)


if __name__ == '__main__':
    main()
