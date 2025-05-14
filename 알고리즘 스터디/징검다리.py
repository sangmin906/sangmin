#시간초과(실패)
t=int(input())
for i in range(t):
    n=int(input())
    sum=1
    num=0
    while True:
        num+=sum
        if n-num<=sum:
            print(sum)
            break
        sum+=1
#이분탐색 키워드가 있던데 이분탐색으로 어떻게 접근할지 모르겠음.