import sys

def add(data, x):
    return data | (1 << x)

def remove(data, x):
    return data & ~(1 << x)

def check(data, x):
    return 1 if (data & (1 << x)) != 0 else 0

def toggle(data, x):
    return data ^ (1 << x)

def all(data):
    return (1 << 21) - 1

def empty():
    return 0

N = int(sys.stdin.readline().rstrip())
data = 0

for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == "add":
        data = add(data, int(command[1]))

    elif command[0] == "remove":
        data = remove(data, int(command[1]))

    elif command[0] == "check":
        sys.stdout.write(str(check(data, int(command[1]))) + "\n")

    elif command[0] == "toggle":
        data = toggle(data, int(command[1]))

    elif command[0] == "all":
        data = all(data)

    elif command[0] == "empty":
        data = empty()