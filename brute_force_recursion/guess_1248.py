n = int (input())
arr = [[0]* n for _ in range(n)]
b= list(input())
v,k= [],0

def possible(idx):
    s= 0 
    for i in range (idx,-1,-1):
        s += v[i]
        # 해당 값이 + 이고 합이 0보다 작은면 false 
        if arr[i][idx] =='+' and s<=0:
            return False
         # 해당 값이 0 이고 합이 0이랑 다르면 false 
        if arr[i][idx] =='0' and s!=0:
            return False
        # 해당 값이 - 이고 합이 0 보다 크면 false 
        if arr[i][idx] == '-' and s>=0:
            return False
    
    return True

def solve(idx) :
    # 종료 조건 
    if idx ==n:
        print(' '.join(map(str,v)))
        exit(0)
    # 음수와 양수 -10 ~10까지 
    for i in range(-10,11):
        v.append(i)
        if possible(idx):
            solve(idx+1)
        v.pop()

# 값 넣기 
#[['-','+','0','+'] 
# [ 0, '+','+','+']
# [ 0,  0, '-','-']
# [ 0,  0,  0, '+']]
for i in range(n):
    for j in range(i,n):
        arr[i][j] = b[k]
        k+=1

# print(arr)
solve(0)