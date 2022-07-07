def sum_param(i, n, s):
    if i > n:
        print(s)
        return
    sum_param(i + 1, n, s + i)


def sum_without_param(n):
    if n == 0:
        return n
    return sum_without_param(n - 1) + n


def main():
    # sum_param(0, 5, 0)
    print(sum_without_param(5))


if __name__ == '__main__':
    main()
