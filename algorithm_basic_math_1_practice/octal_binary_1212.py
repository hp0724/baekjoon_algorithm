n = input()
n = "0o" + n
n = int(n, 8)
print(bin(n).replace("0b", ""))
