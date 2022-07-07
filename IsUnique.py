# determine if a string has all unique characters
# if you cannot use additional ds

def find_unique_using_set(str_non_unq):
    unq_elem = set()
    for elem in str_non_unq:
        if elem in unq_elem:
            print('Not Unique')
            return
        unq_elem.add(elem)
    print('Unique')


def find_unique_using_sort(str_non_unq):
    str_non_unq = list(str_non_unq)
    str_non_unq.sort()
    for idx in range(1,len(str_non_unq)):
        if str_non_unq[idx] == str_non_unq[idx-1]:
            print('Not Unique')
            return
    print('Unique')


if __name__ == '__main__':
    str_non_unq = 'abca'
    # find_unique_using_set(str_non_unq)
    find_unique_using_sort(str_non_unq)