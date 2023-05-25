import sys
n=int(input())
stack=[]
output=[]
 

for _ in range(n):
    n=sys.stdin.readline().split()
    if n[0]=='push':
        stack.append(n[1])
    
    elif n[0]=='top':
        if stack:
            output.append(stack[-1])
        else:
            output.append(-1)
             
    
    elif n[0]=='size':
        output.append(len(stack))
    
    elif n[0]=='pop':
        if stack:
            output.append(stack.pop())
        else:
            output.append(-1)
    
    elif n[0]=='empty':
        if stack:
            output.append(0)
        else:
            output.append(1)

print('\n'.join(map(str,output)))