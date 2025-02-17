def print_board(board):
    for row in board:
        print(" ".join(["Q" if cell else "." for cell in row]))
    print()

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col]:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j]:
            return False
    return True

def solve_n_queens(board, row, n):
    if row == n:
        print_board(board)
        return True
    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = True
            res = solve_n_queens(board, row + 1, n) or res
            board[row][col] = False
    return res

def n_queens(n):
    board = [[False for _ in range(n)] for _ in range(n)]
    if not solve_n_queens(board, 0, n):
        print("Solution does not exist.")

n_queens(8)
