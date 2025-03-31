from collections import deque
n=int(input())
queue=[]
d=deque(queue)
for i in range(n):
    m=input().split()
    if m[0]=="push":
        d.append(m[1])
    elif m[0]=="pop":
        if not d:
            print(-1)
        else:
            a=d.popleft()
            print(a)
    elif m[0]=="size":
        print(len(d))
    elif m[0]=="empty":
        if not d:
            print(1)
        else:
            print(0)
    elif m[0]=="front":
        if not d:
            print(-1)
        else:
            print(d[0])
    elif m[0]=="back":
        if not d:
            print(-1)
        else:
            print(d[-1])