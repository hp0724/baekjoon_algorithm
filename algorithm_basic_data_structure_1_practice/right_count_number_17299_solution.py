from collections import Counter

# 입력
n = int(input())
nums = list(map(int, input().split()))

# 등장 횟수 세기
counter = Counter(nums)
# 결과를 저장할 리스트
answer = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and counter[nums[stack[-1]]] < counter[nums[i]]:
        answer[stack.pop()] = nums[i]
    stack.append(i)

print(" ".join(map(str, answer)))
