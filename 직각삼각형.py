while 1:
    n=list(map(int,input().split()))
    if n==[0,0,0]:
        break
    n.sort()
    if n[0]+n[1]>n[2] and n[0]**2+n[1]**2==n[2]**2:
        print("right")
    else:
        print("wrong")