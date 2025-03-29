n=int(input())
for i in range(n*2-1):
    if i<n:
        for j in range(n*2):
            if j<n-i-1:
                print(" ",end="")
            elif n-i-1<=j<=n+i-1:
                print("*",end="")
    else:
        for j in range(n*2):
            if j<i-n+1:
                print(" ",end="")
            elif i-n+1<=j<=n*3-i-3:
                #n*2-i+(n-3)
                print("*",end="")
    print()