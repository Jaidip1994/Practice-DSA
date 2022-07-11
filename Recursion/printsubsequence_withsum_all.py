def print_subsequence_sum(idx, cur_arr, arr, csum, nsum):
    if idx == len(arr):
        if csum == nsum:
            print(cur_arr)
        return
    csum += arr[idx]
    cur_arr.append(arr[idx])
    print_subsequence_sum(idx + 1, cur_arr, arr, csum, nsum)
    csum -= cur_arr.pop()
    print_subsequence_sum(idx + 1, cur_arr, arr, csum, nsum)


def main():
    arr = [1, 2, 1]
    print_subsequence_sum(0, [], arr, 0, 2)


if __name__ == '__main__':
    main()
