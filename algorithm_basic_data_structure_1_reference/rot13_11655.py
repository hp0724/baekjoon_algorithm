import sys

s = sys.stdin.readline().rstrip()
array = []
for c in s:
    if c.isupper():
        c = ord(c)
        c += 13
        if c > 90:
            c = c - ord("Z") + ord("A") - 1
        c = chr(c)
        array.append(c)
    elif c.islower():
        c = ord(c)
        c += 13
        if c > 122:
            c = c - ord("z") + ord("a") - 1
        c = chr(c)
        array.append(c)
    else:
        array.append(c)

print("".join(map(str, array)))
