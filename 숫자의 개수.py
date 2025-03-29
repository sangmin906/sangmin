a=int(input())
b=int(input())
c=int(input())
n=list(str(a*b*c))
s=0
for i in range(10):
    for j in range(len(n)):
        if i==int(n[j]):
            s+=1
    print(s)
    s=0