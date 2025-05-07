#변수 입력
n=int(input())
p=list(map(int,input().split()))

p=sorted(p) #오름차순 정렬
sum=0
little_sum=0

for i in range(n):
    little_sum+=p[i] #각 개인이 걸리는 시간 합
    sum+=little_sum #총 걸리는 시간 합
print(sum)