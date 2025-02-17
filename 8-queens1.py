def print_solution(board):
    for row in board:
        print(" ".join(["Q" if x else "." for x in row]))
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

def solve(board, row, n):
    if row == n:
        print_solution(board)
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve(board, row + 1, n):
                return True
            board[row][col] = 0
    return False

def n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve(board, 0, n):
        print("Solution does not exist.")

n_queens(8)
