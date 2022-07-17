def ret_possible_perm(pstr):
    res = []

    def perm_str(final_str, prefix):
        if len(final_str) == 0:
            res.append(prefix[:])
        for i in range(0, len(final_str)):
            rem = final_str[:i] + final_str[i + 1:]
            perm_str(rem, prefix + [final_str[i]])

    perm_str(pstr, [])
    return res


def ret_possible_perm_swap(pstr):
    res = []

    def swap_val(idx, pstr):
        if idx == len(pstr):
            res.append(pstr[:])
        for i in range(idx, len(pstr)):
            pstr[i], pstr[idx] = pstr[idx], pstr[i]
            swap_val(idx + 1, pstr)
            pstr[i], pstr[idx] = pstr[idx], pstr[i]

    swap_val(0, pstr)
    return res


def main():
    pstr = [1, 2, 3]
    # print(ret_possible_perm(pstr))
    print(ret_possible_perm_swap(pstr))


if __name__ == '__main__':
    main()
