a, b = map(int, input().split())  # 17 8
digit = int(input())  # 2
stack = []

result = 0
nums = list(map(int, input().split()))
for num in nums:
    result += num * (a ** (digit - 1))
    digit -= 1


while result:
    stack.append(result % b)
    result = result // b

while stack:
    print(stack.pop(), end=" ")
