print("Enter the number of queens")
N = int(input())
board = [[0] * N for _ in range(N)]


def is_attack(i, j):
    
    for k in range(N):
        if board[i][k] == 'Q' or board[k][j] == 'Q':
            return True
    
    for k in range(N):
        for l in range(N):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 'Q':
                    return True
    return False


def N_queen(n):
    if n == 0:
        return True
    for i in range(N):
        for j in range(N):
            if not is_attack(i, j) and board[i][j] != 1:
                board[i][j] = 'Q'
                if N_queen(n - 1):
                    return True
                board[i][j] = 0
    return False


if N_queen(N):
    for i in board:
        print(i)
else:
    print("No solution found.")