print("Enter the number of queens")
N = int(input())
print("Enter the row and column of the first queen (both should be between 0 and N-1)")
first_queen_row = int(input())
first_queen_col = int(input())
board = [[0] * N for _ in range(N)]
board[first_queen_row][first_queen_col] = 'Q'
def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
def is_attack(i, j, board):
    N = len(board)
    for k in range(N):
        if board[i][k] == 'Q' or board[k][j] == 'Q':
            return True
    for k in range(N):
        for l in range(N):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 'Q':
                    return True
    return False                  
def N_queen(n, board):
    if n == 0:
        return True
    N = len(board)
    for i in range(N):
        for j in range(N):
            if not is_attack(i, j, board) and board[i][j] != 'Q':
                board[i][j] = 'Q'
                if N_queen(n - 1, board):
                    return True
                board[i][j] = 0
    return False
if N_queen(N - 1, board):
    print("Solution:")
    print_board(board)
else:
    print("No solution found.")