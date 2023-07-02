from itertools import combinations
array=[]
LOTTO_NUMBER= 6
while True:
    array=list(map(int,input().split()))
    if(array[0]==0):
        break
    array.pop(0)    
    for i in list(combinations(array,LOTTO_NUMBER)):
        print(" ".join(map(str,i)))
    
    print()
    