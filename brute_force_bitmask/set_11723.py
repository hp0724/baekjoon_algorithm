M =int(input())
data=[]
data=set(data)
result=[]
for _ in range(M):
    cmd= input().split()
     
    if cmd[0]=='add':
        data.add(int(cmd[1]))
         
    elif cmd[0]== 'check':
         
        if int(cmd[1]) in data:
            result.append(1)
        else:
            result.append(0)
    elif cmd[0]=='remove':
        if int(cmd[1]) in data:
            data=list(data)
            idx=data.index(int(cmd[1]))
            data.pop(int(idx))
            
            # data.remove(int(cmd[1]))
    elif cmd[0] =='toggle':
        if int(cmd[1])in data:
            data=list(data)
            idx=data.index(int(cmd[1]))
            data.pop(int(idx))
            # data.remove(int(cmd[1]))
        else:
            data.add(int(cmd[1]))

    elif cmd[0] == 'all':
        data=[i for i in range(1,21)]
        data=set(data)
         
    elif cmd[0] == 'empty':
        data.clear()
         
print("\n".join(map(str,result)))
# 11010101100010
# 1101010101100010