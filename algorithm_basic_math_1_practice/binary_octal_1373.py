n = list(input())
sum = 0
i = 0
while n:
    sum = sum + (int(n.pop()) * (2**i))
    i += 1

result = oct(sum).replace("0o", "")
print(result)
