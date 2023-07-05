n= int (input()) 
sign =list(input().split())
# 10개의 숫자 
visited= [False]* 10 

max_ans ,min_ans ="",""

# 연산자 계산 
def possible(i,j,k):
    if k == '<':
        return i<j
    else : 
        return i>j 
    return True 

# 최대값과 최솟값 구하기 

def solve (cnt,s):
    global min_ans , max_ans 

    # 종료 조건 부등호 개수 + 1 문자열 

    if cnt ==n+1 : 
        # 최솟값이 존재하지 않는다면  
        if not len(min_ans):
            min_ans=s 
        # 그 외에는 최대값 
        else :
            max_ans = s 
        return 
    
    for i in range(10):
        if not visited[i]:
            # 문자열이 아직 존재하지 않거나 ,계산이 가능한 경우 
            # s[-1]을 통해서 s 의마지막 값과 
            # 반복문의 i를 가져와서 possible 매개변수로 넘겨주기 
            if cnt ==0 or possible(s[-1],str(i),sign[cnt-1]):
                visited[i]=True
                solve(cnt+1,s+str(i))
                visited[i] =False


solve(0,"")
print(max_ans)
print(min_ans)