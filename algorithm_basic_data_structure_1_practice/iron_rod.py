data = input()
data = data.replace("()", "*")
stack = []
result = 0
for i in data:
    if i == "(":
        stack.append(i)

    elif i == ")":
        stack.pop()
        result += 1

    elif i == "*":
        if stack:
            result += len(stack)
print(result)
