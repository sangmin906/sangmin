n=int(input())
m=list(map(int,input().split()))
s=0
for i in range(n):
    if m[i]!=1 and m[i]!=0:
        if m[i]%m[i]==0 and all(m[i]%j!=0 for j in range(2,m[i])):
            s+=1
print(s)