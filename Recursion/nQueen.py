final_result = []


def check_ideal_place(row, col, board, n):
    temp_r = row
    temp_c = col

    # Checking all the columns and keeping the row constant
    while col >= 0:
        if board[row][col] == 'Q':
            return False
        col -= 1

    row = temp_r
    col = temp_c

    # Moving across the top right diagonal
    while row >= 0 and col >= 0:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col -= 1

    row = temp_r
    col = temp_c

    # Moving across the top right diagonal
    while row < n and col >= 0:
        if board[row][col] == 'Q':
            return False
        row += 1
        col -= 1

    return True


def solve(col, board, n):
    if col == n:
        final_result.append(["".join(row) for row in board])
        return
    for row in range(0, n):
        if check_ideal_place(row, col, board, n):
            board[row][col] = 'Q'
            solve(col + 1, board, n)
            board[row][col] = '.'


def main():
    n = 1
    row_board = ["." for _ in range(n)]
    board = []
    for _ in range(n):
        board.append(row_board[:])
    solve(0, board, n)
    print(final_result)


if __name__ == '__main__':
    main()
