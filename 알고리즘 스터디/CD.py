while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    N=set([int(input()) for i in range(n)])
    M=set([int(input()) for j in range(m)])
    print(len(N&M))