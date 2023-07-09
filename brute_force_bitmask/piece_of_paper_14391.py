import sys

def get_max_sum(n, m, paper):
    max_sum = 0

    for state in range(1 << (n * m)):
        sum = 0
        for i in range(n):
            row_sum = 0
            for j in range(m):
                # 2차원 배열을 1차원 배열로 옮긴것 
                idx = i * m + j
                 
                # 가로로 자르는 경우
                if (state & (1 << idx)) == 0:
                    row_sum = row_sum * 10 + paper[i][j]
                else:
                    sum += row_sum
                    row_sum = 0

            # 남은 가로 조각의 합을 더함
            sum += row_sum

        # 세로 조각의 합을 더함
        for j in range(m):
            col_sum = 0
            for i in range(n):
                # 2차원 배열을 1차원 배열로 옮긴것 
                idx = i * m + j

                # 세로로 자르는 경우
                if (state & (1 << idx)) != 0:
                    col_sum = col_sum * 10 + paper[i][j]
                else:
                    sum += col_sum
                    col_sum = 0

            # 남은 세로 조각의 합을 더함
            sum += col_sum

        max_sum = max(max_sum, sum)

    return max_sum


# 입력 받기
n, m = map(int, sys.stdin.readline().split())
paper = []
for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().strip())))

# 최대 합 구하기
result = get_max_sum(n, m, paper)
print(result)

 