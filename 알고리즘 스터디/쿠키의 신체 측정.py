n=int(input())
a=[0]*n
s=0
h=0
l=0
for i in range(n):
    b=list(input())
    a[i]=b
for j in range(n):
    for k in range(n):
        if a[j][k]=="*":
            h+=1
            s+=1
            if h==1:
                c=[j+2,k+1]
                print(j+2,k+1)
                s=0
            if j==c[0] and k==c[1]:
                print(h-1,end=" ")
                s=0
            elif j==c[0] and k==n-1:
                print(s,end=" ")
                s=0
            elif h>4 and k!=c[1]:
                print(s,end="")
                s=0
#다리는 어떻게 해야할지 모르겠음/애초에 어디서 오답인지 모르겠음