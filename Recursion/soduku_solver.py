def soduku_solver(board):
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == '.':
                for k in range(1, 10):
                    if cor_pos(i, j, str(k), board):
                        board[i][j] = str(k)
                        if soduku_solver(board):
                            return True
                        else:
                            board[i][j] = '.'
                return False
    return True


def cor_pos(row, col, c, board):
    for i in range(0, 9):

        # Check for all the rows
        if board[i][col] == c:
            return False

        # Check for all the columns
        if board[row][i] == c:
            return False

        # Check inside the 3*3 square box
        if board[3 * (row // 3) + (i // 3)][3 * (col // 3) + (i % 3)] == c:
            return False
    return True


def main():
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    soduku_solver(board)
    print(board)


if __name__ == '__main__':
    main()
