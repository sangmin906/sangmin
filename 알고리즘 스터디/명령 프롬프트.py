n=int(input())
for i in range(n):
    if i==0:
        m=list(input())
    elif i>=1:
        k=list(input())
        for j in range(len(m)):
            if m[j]!=k[j]:
                m[j]="?"
print(''.join(m))
