def countsubseq_with_cnt(carr, arr, idx, csum, asum):
    if idx == len(arr):
        if csum == asum:
            return 1
        return 0
    csum += arr[idx]
    carr.append(arr[idx])
    l = countsubseq_with_cnt(carr, arr, idx + 1, csum, asum)
    csum -= carr.pop()
    r = countsubseq_with_cnt(carr, arr, idx + 1, csum, asum)
    return l + r


def main():
    arr = [1, 2, 1]
    print(countsubseq_with_cnt([], arr, 0, 0, 2))


if __name__ == '__main__':
    main()
