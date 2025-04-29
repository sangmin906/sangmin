n=int(input())
N=list(map(int,input().split()))
m=int(input())
M=list(map(int,input().split()))

#오름차순으로 배열
N=sorted(N)

#수 찾기
for select in M:
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if select==N[mid]:
            print(1)
            break
        elif select<N[mid]:
            high=mid-1
        elif select>N[mid]:
            low=mid+1
    if low>high:
        print(0)