#모듈 설정
import sys
input=sys.stdin.readline #읽기 최적화
from bisect import bisect_left, bisect_right #이분탐색 최적화

#입력
n=int(input())
N=sorted(list(map(int,input().split())))
m=int(input())
M=list(map(int,input().split()))

#이분탐색
for i in range(m):
    low=0
    high=n-1
    while low<=high: #high가 low보다 클 때만 반복
        mid=(low+high)//2
        if N[mid]==M[i]:
            print(bisect_right(N,M[i])-bisect_left(N,M[i]),end=" ") #중복되는 수의 왼쪽 위치와 오른쪽 위치 찾아 둘 사이의 간격 구하기
            break
        elif N[mid]<M[i]:
            low=mid+1
        elif N[mid]>M[i]:
            high=mid-1
    if low>high:
        print(0,end=" ")