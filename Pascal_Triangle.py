def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    res = [[1], [1, 1]]
    for i in range(1, numRows):
        temp_arr = []
        for j in range(1, len(res[i])):
            temp_arr.append(res[i][j] + res[i][j - 1])
        res.append([1] + temp_arr + [1])
    return res[:numRows]


if __name__ == '__main__':
    print(generate(5))
