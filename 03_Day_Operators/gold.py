x=int(input())
j,k,l,m=map(int,input().split())
thomas=j+k+l+m
rank=0
for i in range(1,x):
    j,k,l,m=map(int,input().split())
    score=j+k+l+m
    if score>thomas:
        rank+=1
print(rank+1)