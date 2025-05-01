a,b=map(int,input().split())
if a<b:
    a,b=b,a
if a-b==0:
    print(a-b)
else:
    print(a-b-1)
    if a-b!=1:
        for i in range(b+1,a):
            print(i,end=" ")