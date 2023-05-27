t_c= int(input())
 
for _ in range(t_c):
    data=input()
    stack=[]

    for bracket in data:
        if bracket=='(':
            stack.append(bracket)
        else:
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                print('NO')
                break
    else:

        if stack:
            print('No')
        else:
            print('YES')
        


     
 
     

    