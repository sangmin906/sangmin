n,m=map(int,input().split())
a=list(map(int,input().split()))
s=0
a.sort(reverse=True)
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if a[i]+a[j]+a[k]==m:
                print(m)
                exit()
            elif a[i]+a[j]+a[k]<m:
                if s<a[i]+a[j]+a[k]:
                    s=a[i]+a[j]+a[k]
print(s)