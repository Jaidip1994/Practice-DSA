def countsubseq_with_dup(idx, rsum, carr, arr):
    if idx == len(arr):
        if rsum == 0:
            print(carr)
        return
    if arr[idx] <= rsum:
        carr.append(arr[idx])
        countsubseq_with_dup(idx + 1, rsum - arr[idx], carr, arr)
        carr.pop()
    countsubseq_with_dup(idx + 1, rsum, carr, arr)


def countsubseq_unq(idx, target, carr, oarr):
    if target == 0:
        print(carr)
        return
    for i in range(idx, len(oarr)):
        if i > idx and oarr[i] == oarr[i - 1]:
            continue
        if oarr[i] > target:
            break
        carr.append(oarr[i])
        countsubseq_unq(i + 1, target - oarr[i], carr, oarr)
        carr.pop()


def main():
    candidate = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    # countsubseq_with_dup(0, target, [], candidate)
    candidate.sort()
    countsubseq_unq(0, target, [], candidate)


if __name__ == "__main__":
    main()
