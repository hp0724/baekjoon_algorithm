n = int(input())
data = list(map(int, input().split()))
right_big_number = [-1] * n  # 결과를 저장할 리스트, 초기값은 -1로 설정

stack = []  # 인덱스를 저장할 스택
# 3 5 2 7
# 오른쪽에 있는 큰 수 찾기
for i in range(n):
    # 스택에 값이있고 기준값보다 큰 경우
    while stack and data[stack[-1]] < data[i]:
        right_big_number[stack.pop()] = data[i]
    stack.append(i)

print(" ".join(map(str, right_big_number)))
