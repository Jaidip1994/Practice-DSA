# Here num & (1 << i) is checking whether the ith bit is set or not

def powerset(str_c):
    n = len(str_c)
    for num in range(1 << n):
        subs = ""
        for i in range(n):
            if (num & (1 << i)) > 0:
                subs += str_c[i]
        print(subs)


def main():
    powerset("abc")


if __name__ == '__main__':
    main()
