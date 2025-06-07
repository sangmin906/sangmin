#입력
n=int(input())
t=list(map(int,input().split()))

#변수 설정
t.sort(reverse=True) #왼쪽부터 가장 오래 걸리는 순서로 심기
Max=-100000 #나무 묘목 개수 n이 100,000이고, 자라는 시간 t가 모두 1인 극단적인 경우를 대비하고자 -100,000로 설정
num=0

#왼쪽부터 가장 오래 걸리는 순서로 심었다는 가정 하에, 내림차순인 t에 자라는데 걸리는 일수를 뺐을 때 가장 큰 수를 구하기
for i in range(n,0,-1):
    if Max<t[num]-i:
        Max=t[num]-i
    num+=1

#위에서 구한 가장 큰 수와 n과 1(묘목을 구입한 날), 1(이장님 초대하는 날)을 더해서 출력
print(n+Max+2)