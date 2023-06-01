# 문자열 N개가  소문자,대문자,숫자,공백
import sys

# "a" = 97 "z" 122 'A' =65 'Z'=90  ' ' = 32

while True:
    expression = sys.stdin.readline().strip("\n")
    # EOF 처리
    if not expression:
        break
    small_letter = 0
    capital_letter = 0
    number = 0
    blank = 0

    for i in expression:
        if ord(i) >= 97 and ord(i) <= 122:
            small_letter += 1
        elif ord(i) >= 65 and ord(i) <= 90:
            capital_letter += 1
        elif ord(i) >= 48 and ord(i) <= 57:
            number += 1
        elif ord(i) == 32:
            blank += 1
    print(small_letter, capital_letter, number, blank)
