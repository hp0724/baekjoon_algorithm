from itertools import permutations

n = int(input())
permutations_array = list(map(int,input().split()))
permutations_list=list(permutations(sorted(permutations_array),n))

 
for idx,value in enumerate( permutations_list):
    if permutations_array == list(value): 
        if idx+1==len(permutations_list):
            print(-1)
            break
        if idx<len(permutations_list):
            print(" ".join(map(str,permutations_list[idx+1])))
  