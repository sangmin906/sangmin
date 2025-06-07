#모듈 설정
from bisect import bisect_left

#입력
n,k=map(int,input().split())
n_list=[int(input()) for i in range(n)]

if k in n_list: #목표금액 k가 가지고 있는 동전들(n_list) 중 하나일 때
    print(1)
else: #목표금액 k가 가지고 있는 동전(n_list)이 아닐 때
    #변수 설정
    sum=0 #동전 금액의 합
    num=0 #동전의 갯수
    m=bisect_left(n_list,k) #가지고 있는 동전들(n_list) 중에서 k를 넘지 않는 가장 금액이 큰 동전
    
    for i in range(m-1,-1,-1): #k를 넘지 않는 가장 금액이 큰 동전부터 금액이 작은 동전까지 차례대로 더하기
        while sum<k: #동전 금액의 합이 목표금액 k를 넘지 않을 때까지 반복
            sum+=n_list[i]
            num+=1
            if sum>k: #목표금액 k를 넘었을 경우
                sum-=n_list[i] #바로 위에서 더했던 합과 갯수 다시 빼기
                num-=1
                break #금액이 조금 더 낮은 다른 동전으로 목표금액 채우기
            elif sum==k: #목표금액 k에 도달했을 경우
                print(num) #동전의 갯수 출력
                break
        if sum==k: #목표금액 k에 도달했을 경우 루프(반복) 빠져나가기
            break