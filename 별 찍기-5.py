n=int(input())
for i in range(n):
    for j in range(1,n*2):
        if j>=n-i and j<=n+i:
            print("*",end="")
        else:
            print(" ",end="")
    print()