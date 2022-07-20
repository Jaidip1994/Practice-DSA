def fibonacci(n, fib_arr):
    if n <= 1:
        return n
    if fib_arr[n] != -1:
        return fib_arr[n]
    fib_arr[n] = fibonacci(n - 1, fib_arr) + fibonacci(n - 2, fib_arr)
    return fib_arr[n]


def recurssion_top_dwn(n):
    fib_arr = [-1 for _ in range(n + 1)]
    print(fibonacci(n, fib_arr))

def dp_tabular(n):
    prev1, prev2 = 0, 1
    for i in range(2,n+1):
        prev1, prev2 = prev2, prev1 + prev2
    return prev2


def main():
    n = 5
    recurssion_top_dwn(n)
    print(dp_tabular(n))


if __name__ == '__main__':
    main()
