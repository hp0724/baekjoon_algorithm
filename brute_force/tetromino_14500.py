import sys

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
grid = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    grid.append(row)

# 테트로미노 모양 정의
tetrominoes = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # -
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # |
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # ㅁ
    [(0, 0), (1, 0), (2, 0), (2, 1)],  # L
    [(0, 0), (1, 0), (2, 0), (2, -1)],  # L 반대
    [(0, 0), (1, 0), (2, 0), (0, 1)],  # L 회전
    [(0, 0), (1, 0), (2, 0), (0, -1)],  # L 회전 반대
    [(0, 0), (0, 1), (0, 2), (1, 0)],  # ㄴ
    [(0, 0), (0, 1), (0, 2), (-1, 0)],  # ㄴ 반대
    [(0, 0), (0, 1), (1, 1), (1, 2)],  # 번개
    [(0, 0), (1, 0), (1, -1), (2, -1)],  # 번개 회전
    [(0, 0), (1, 0), (1, 1), (2, 1)],  # 번개 반대
    [(0, 0), (0, 1), (-1, 1), (-1, 2)],  # 번개 반대 회전
    [(0, 0), (1, 0), (1, -1), (2, 0)],  # ㄹ
    [(0, 0), (0, 1), (-1, 1), (0, 2)],  # ㄹ 반대
    [(0, 0), (1, 0), (1, 1), (2, 0)],  # ㄹ 회전
    [(0, 0), (0, 1), (-1, 1), (0, -1)],  # ㄹ 회전 반대
    [(0, 0), (0, 1), (0, -1), (1, 0)],  # ㅗ
    [(0, 0), (0, 1), (0, -1), (-1, 0)],  # ㅜ
    [(0, 0), (1, 0), (-1, 0), (0, -1)],  # ㅓ
    [(0, 0), (1, 0), (-1, 0), (0, 1)],  # ㅏ
]

# 최대 합 구하기
max_sum = 0
for i in range(n):
    for j in range(m):
        for tetromino in tetrominoes:
            tet_sum = 0
            for dx, dy in tetromino:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < m:
                    tet_sum += grid[nx][ny]
                else:
                    tet_sum = 0
                    break
            max_sum = max(max_sum, tet_sum)

print(max_sum)
