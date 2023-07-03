# 한개의 모음 
# 두개의 자음 최소 값 
# 오름차순 
# 자음 모음 나눠서 진행후 붙이기 
from itertools import combinations
L,C = map(int,input().split())
alphabets=input().split()
#자음
consonants=[]
#모음
vowels=[]

consonants_array=[]
vowels_array=[]
password_array=[]
 
for i in alphabets:
    if i in ['a','e','i','o','u']:
        vowels.append(i)
    else:
        consonants.append(i)

vowels.sort()
consonants.sort()

# 최소 1개의 모음과 최소 2개의 자음을 선택한 후 조합 생성
for i in range(1, len(vowels) + 1):
    for j in combinations(vowels, i):
        if L - i >= 2:
            for k in combinations(consonants, L - i):
                password_array.append(''.join(sorted(list(k + j))))

# 비밀번호 리스트를 오름차순으로 정렬
password_array.sort()

# 출력
for password in password_array:
    print(password)

 