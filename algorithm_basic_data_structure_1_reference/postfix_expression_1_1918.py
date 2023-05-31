word = input()
operator = []
operand = []
for i in word:
    if i.isalpha():
        operand.append(i)
    elif i != "(" and i != ")" and not i.isalpha():
        operator.append(i)

print(operator)
operator.reverse()
print(operand + operator)
