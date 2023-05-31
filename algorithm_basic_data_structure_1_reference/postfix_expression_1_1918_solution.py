def precedence(op):
    if op == "+" or op == "-":
        return 1
    if op == "*" or op == "/":
        return 2
    return 0


def infix_to_postfix(expression):
    stack = []
    postfix = ""
    # A+B*C-D/E
    for char in expression:
        if char.isalpha():
            postfix += char
        elif char == "(":
            stack.append("(")
        elif char == ")":
            # ( 값이 아니면 postfix에 추가
            while stack and stack[-1] != "(":
                postfix += stack.pop()
            stack.pop()
        else:
            while stack and precedence(char) <= precedence(stack[-1]):
                postfix += stack.pop()
            stack.append(char)
    while stack:
        postfix += stack.pop()
    return postfix


expression = input()
postfix_expression = infix_to_postfix(expression)
print(postfix_expression)
