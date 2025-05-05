a,b=map(int,input().split())
if a<b:
    a,b=b,a
if a-b==0:
    print(a-b)
a=list(map(int,input().split()))
if a[0]<a[1]:
    big=a[1]
    small=a[0]
elif a[0]>a[1]:
    big=a[0]
    small=a[1]
else:
    print(a-b-1)
    if a-b!=1:
        for i in range(b+1,a):
    print(a[0]-a[1])
    exit()
if big-small>=1:
    print(big-small-1)
    if big-small!=1:
        for i in range(small+1,big):
            print(i,end=" ")