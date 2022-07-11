def print_subsequence_sum_all(carr, clen, arr, csum, nsum):
    if clen == len(arr):
        if csum == nsum:
            print(carr)
            return True
        return False
    csum += arr[clen]
    carr.append(arr[clen])
    if print_subsequence_sum_all(carr, clen + 1, arr, csum, nsum):
        return True
    csum -= carr.pop()
    if print_subsequence_sum_all(carr, clen + 1, arr, csum, nsum):
        return True


def main():
    arr = [1, 2, 1]
    print_subsequence_sum_all([], 0, arr, 0, 2)


if __name__ == "__main__":
    main()
