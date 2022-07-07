# Print 5 - 1 using backtracking
def recr_func(i, n):
    if i > n:
        return
    recr_func(i + 1, n)
    print(i)


def main():
    recr_func(1, 5)


if __name__ == "__main__":
    main()
