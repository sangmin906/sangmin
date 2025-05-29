n=int(input())
for i in range(n):
    print(" "*i,end="")
    for j in range(2*n):
        if j<(2*n)-1-(i*2):
            print("*",end="")
    print("")