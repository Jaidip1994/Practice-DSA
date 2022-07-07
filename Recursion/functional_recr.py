def reverse_str(start, end, str_to_reverse):
    if start > end:
        return str_to_reverse
    reverse_str(start + 1, end - 1, str_to_reverse)
    str_to_reverse[start], str_to_reverse[end] = str_to_reverse[end], str_to_reverse[start]
    return str_to_reverse

def main():
    str_to_reverse = 'jaidip'
    fnd_str = reverse_str(0, len(str_to_reverse) - 1, list(str_to_reverse))
    print("".join(fnd_str))


if __name__ == '__main__':
    main()