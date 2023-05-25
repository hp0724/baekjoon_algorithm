import sys

t_c = int(input())
for _ in  range(t_c):
    str = sys.stdin.readline().split()
    array=''
    for i in str:
        i=list(i)
        i.reverse()
        i=''.join(i)
        array+=i+' '

        
    
    print(array)

    
     