def fibonacci_with_loop(n):
    final_ar = [0, 1]
    for i in range(2, n+1):
        final_ar.append(final_ar[i - 1] + final_ar[i - 2])
    print(final_ar)
    return final_ar[i]


def fibonacci_with_recr(n):
    if n <= 1:
        return n
    return fibonacci_with_recr(n - 1) + fibonacci_with_recr(n - 2)


def main():
    print(f'With loop: {fibonacci_with_loop(5)}')
    print(f'With Recr: {fibonacci_with_recr(5)}')


if __name__ == '__main__':
    main()
