n = input()
n = "0b" + n
n = int(n, 2)
n = oct(n)
print(n.replace("0o", ""))
