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
#7번째 줄에 NoneType이라는데 이게 왜 타입이 정해져있지 않은지 모르겠음n=int(input()) #5
N=list(map(int,input().split())) #6 3 2 10 -10
m=int(input()) #8
M=list(map(int,input().split())) #10 9 -5 2 3 4 5 -10

#오름차순으로 설정
#sort()함수는 원본 리스트의 리턴값이 None, sorted()함수는 리턴값이 출력
N=sorted(N) #-10 2 3 6 10

#변수 설정
output=[0]*m
index=0

#이분탐색으로 숫자 카드 탐색
for select in M:
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if select==N[mid]:
            output[index]=1
            break
        elif select<N[mid]:
            high=mid-1
        elif select>N[mid]:
            low=mid+1
    index+=1

#출력
print(*output)