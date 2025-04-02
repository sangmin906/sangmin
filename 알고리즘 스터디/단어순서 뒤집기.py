n=int(input())
for i in range(n):
    m=list(input().split())
    print(f"Case #{i+1}:",*m[::-1])
    #print("Case #{}:".format(i+1),*m[::-1])도 가능
