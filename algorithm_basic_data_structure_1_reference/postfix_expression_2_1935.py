n = int(input())
word = input()
num_lst = [0] * n

for i in range(n):
    num_lst[i] = int(input())

stack = []

for i in word:
    if i.isAlpha():
        stack.append(num_lst[ord(i) - ord("A")])
    else:  # 연산자를 만나면
        str2 = stack.pop()
        str1 = stack.pop()

        if i == "+":
            stack.append(str1 + str2)
        elif i == "-":
            stack.append(str1 - str2)
        elif i == "*":
            stack.append(str1 * str2)
        elif i == "/":
            stack.append(str1 / str2)

print("%.2f" % stack[0])
