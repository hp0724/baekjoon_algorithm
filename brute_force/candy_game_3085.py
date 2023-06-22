def solve(board, n):
    max_candies = 1
    # 01  01  02
    # 10 20
    for i in range(n):
        for j in range(n - 1):
            if board[i][j] != board[i][j + 1]:
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
                max_candies = max(max_candies, check_max_candies(board, n))
                # 다시 되돌리기
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            if board[j][i] != board[j + 1][i]:
                board[j][i], board[j + 1][i] = board[j + 1][i], board[j][i]
                max_candies = max(max_candies, check_max_candies(board, n))
                # 다시 되돌리기
                board[j][i], board[j + 1][i] = board[j + 1][i], board[j][i]
    return max_candies


def check_max_candies(board, n):
    max_candies = 1

    for i in range(n):
        row_candies = 1
        col_candies = 1
        for j in range(n - 1):
            # 세로 방향 체크
            # 같은 색깔인 경우
            if board[i][j] == board[i][j + 1]:
                col_candies += 1
            # 다른 색깔인 경우
            else:
                max_candies = max(max_candies, col_candies)
                col_candies = 1

            # 가로 방향 체크
            # 같은 색깔인 경우
            if board[j][i] == board[j + 1][i]:
                row_candies += 1
            # 다른 색깔인 경우
            else:
                max_candies = max(max_candies, row_candies)
                row_candies = 1
        max_candies = max(max_candies, row_candies, col_candies)
    return max_candies


n = int(input())
board = []

for i in range(n):
    row = list(input())
    board.append(row)
# print(board)

result = solve(board, n)
print(result)
