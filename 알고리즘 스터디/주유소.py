#입력
n=int(input())
d=list(map(int,input().split()))
p=list(map(int,input().split()))

#변수 설정
output=0 #최소 비용 변수
Min=p[0] #첫번째 주유소는 무조건 거쳐야하기 때문에 p[0]로 시작

for i in range(n-1):
    if p[i]<Min: #지금까지 나온 주유소 금액 중 가장 최소 금액이라면 Min값 변경
        Min=p[i]
    output+=Min*d[i] #주유소 금액X다음 주유소까지의 거리

#출력
print(output)