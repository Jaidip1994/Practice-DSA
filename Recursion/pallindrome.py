def pallindrome(start, end, str_to_chk):
    if start > end:
        return True
    if str_to_chk[start] != str_to_chk[end]:
        return False
    return pallindrome(start+1, end - 1, str_to_chk)


def main():
    str_chk = 'madap'
    print(pallindrome(0, len(str_chk) - 1, str_chk))


if __name__ == '__main__':
    main()