n=int(input())
if n<=5:
    if n%3==0 or n%5==0:
        print(1)
    else:
        print(-1)
else:
    if n%5==0:
        print(n//5)
    else:
        x=False
        for i in range(n//5,-1,-1):
            for j in range(1,(n//5)+3):
                output=(5*i)+(3*j)
                if n==output:
                    x=True
                    print(i+j)
                    break
            if x:
                break
        if not x:
            print(-1)