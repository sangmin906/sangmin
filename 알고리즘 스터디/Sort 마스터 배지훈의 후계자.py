import sys
from bisect import bisect_left
input=sys.stdin.readline
print=sys.stdout.write

#입력 받기
n,m=map(int,input().split())
N=sorted([int(input()) for i in range(n)])

#정수D를 받으며 이진탐색으로 계산
for j in range(m):
    M=int(input())
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if M==N[mid]: #M과 이진탐색으로 탐색한 수가 일치할 때
            print(f"{bisect_left(N,M)}\n") #탐색한 수가 중복일 때, 가장 왼쪽에 있는 수의 위치 출력
            break
        elif M<N[mid]: #작으면 high 범위 낮추기
            high=mid-1
        elif M>N[mid]:#높으면 low 범위 높이기
            low=mid+1
    if low>high: #M이 N 안에 들어있지 않은 경우, -1출력
        print(f"{-1}\n")