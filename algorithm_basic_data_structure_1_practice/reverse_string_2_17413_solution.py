s = input()
reversed_string = ""
stack = []
is_tag = False

for char in s:
    if char == "<":
        is_tag = True
        while stack:
            reversed_string += stack.pop()
        # < 추가
        reversed_string += char
    elif char == ">":
        is_tag = False
        reversed_string += char
        # tag가 열려있으면 그냥 넣기
    elif is_tag:
        reversed_string += char
        # tag가 닫혀있을때
    else:
        # 띄어쓰기 만나면 그전까지 문자열 뒤집기
        if char == " ":
            while stack:
                reversed_string += stack.pop()
            reversed_string += char
        else:
            stack.append(char)
while stack:
    reversed_string += stack.pop()

print(reversed_string)
