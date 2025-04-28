n=int(input())
N=list(map(int,input().split()))
m=int(input())
M=list(map(int,input().split()))
N=N.sort()
M=M.sort()
mid=(M[0]+M[-1])//2
for i in range(n):
    if N[i]==M[mid]:
        print(1,end=" ")
        break
    elif N[i]<M[mid]:
        M=M[:mid-1]
        mid=(M[0]+M[mid-1])//2
    elif N[i]>M[mid]:
        M=M[mid+1:]
        mid=(M[mid+1]+M[-1])//2
    else:
        print(0,end=" ")
#7번째 줄에 NoneType이라는데 이게 왜 타입이 정해져있지 않은지 모르겠음