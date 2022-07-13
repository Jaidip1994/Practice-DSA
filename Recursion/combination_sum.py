def combination_sum(idx, bval, carr, oarr):
    if idx == len(oarr):
        if bval == 0:
            print(carr)
        return
    if oarr[idx] <= bval:
        carr.append(oarr[idx])
        combination_sum(idx, bval - oarr[idx], carr, oarr)
        carr.pop()
    combination_sum(idx + 1, bval, carr, oarr)


def main():
    arr = [2, 3, 6, 7]
    combination_sum(0, 7, [], arr)


if __name__ == '__main__':
    main()
