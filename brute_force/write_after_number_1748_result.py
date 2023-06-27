n= int(input())

digit =len(str(n)) # 입력된 수의 자릿수 
count = 0

# 1의 자리부터 (digit-1) 까지의 숫자들의 개수 
# 1자리 9 개 
# 2자리 90 *2  개
# 3자리 900 * 3 개  

# n자릿수 -1 까지 더해주기 
for i in range(digit-1):
    count += 9 *10 ** i *(i+1)
     
# n자릿수 개수 더하기 
# 123이면 100까지는 위에서 더하고 101~123 까지 개수 더하기 
count +=(n-10**(digit-1) +1)*digit

print(count)