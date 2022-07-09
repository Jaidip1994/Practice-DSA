def print_subs(idx, n, cur_arr, arr):
    if idx == n:
        print(cur_arr)
        return
    cur_arr.append(arr[idx])
    print_subs(idx + 1, n, cur_arr, arr)
    cur_arr.pop()
    print_subs(idx + 1, n, cur_arr, arr)


def main():
    arr = [3, 1, 2]
    print_subs(0, len(arr), [], arr)


if __name__ == '__main__':
    main()
