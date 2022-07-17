final_arr = []


def subset_pattern_nunq(nums):
    global final_arr
    final_arr = [[]]
    for elem in nums:
        final_arr += [i + [elem] for i in final_arr]
        # print(final_arr)

    temp_set = set(tuple(elem) for elem in final_arr)
    final_arr = [list(elem) for elem in temp_set]


def subset_pattern_unq(idx, carr, oarr):
    final_arr.append(carr[:])
    for i in range(idx, len(oarr)):
        if i > idx and oarr[i] == oarr[i - 1]:
            continue
        carr.append(oarr[i])
        subset_pattern_unq(i + 1, carr, oarr)
        carr.pop()


def main():
    global final_arr
    nums = [4, 4, 4, 1, 4]
    nums.sort()
    subset_pattern_nunq(nums)
    print(final_arr)
    final_arr = []
    print('=' * 20)
    subset_pattern_unq(0, [], nums)
    print(final_arr)


if __name__ == "__main__":
    main()
