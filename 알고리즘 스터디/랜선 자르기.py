#입력
k,n=map(int,input().split())
K=sorted([int(input()) for i in range(k)])

#변수 설정
high=K[-1]
low=1
answer=0 #최적의 길이를 찾기 위해 설정한 변수

#이분탐색
while low<=high:
    mid=(high+low)//2
    num=0 #랜선 갯수
    for i in K:
        num+=i//mid #k개의 랜선을 나누며 갯수 세기
    if num>=n: #n개의 랜선보다 많은 경우
        if mid>answer: #최적의 길이보다 더 최적화된 길이인 경우
            answer=mid #변수에 대입
        low=mid+1 #또 다른 최적의 길이를 찾고자 범위 제한
    elif num<n: #n개의 랜선보다 적은 경우
        high=mid-1 #범위 제한
print(answer) #최적의 길이 출력