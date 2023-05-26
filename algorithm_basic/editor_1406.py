# 커서는 문장 맨뒤에 위치


edit_string = input()
edit_string = list(edit_string)
m = int(input())
point = len(edit_string)


for _ in range(m):
    cmd = input().split()
    if cmd[0] == "P":
        edit_string.insert(point, cmd[1])
        point += 1

    elif cmd[0] == "B":
        if point > 0:
            point -= 1
            edit_string.pop(point)

    elif cmd[0] == "L":
        if point > 0:
            point -= 1

    elif cmd[0] == "D":
        if point < len(edit_string):
            point += 1

print("".join(edit_string))
