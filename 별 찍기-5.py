n=int(input())
for i in range(n):
    for j in range(n*2-1):
        if n-i-1<=j<=n+i-1:
            print("*",end="")
        elif j<=n-i-1:
            print(" ",end="")
    print()