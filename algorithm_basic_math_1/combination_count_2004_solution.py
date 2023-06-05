def count_trailing_zeros(n, base):
    count = 0
    while n >= base:
        n //= base
        count += n
    return count


def count_combination_zeros(n, m):
    count_2 = (
        count_trailing_zeros(n, 2)
        - count_trailing_zeros(m, 2)
        - count_trailing_zeros(n - m, 2)
    )
    count_5 = (
        count_trailing_zeros(n, 5)
        - count_trailing_zeros(m, 5)
        - count_trailing_zeros(n - m, 5)
    )
    return min(count_2, count_5)


n, m = map(int, input().split())

result = count_combination_zeros(n, m)
print(result)
# 25 12
