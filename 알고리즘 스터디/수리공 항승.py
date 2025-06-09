#입력
n,l=map(int,input().split())
s=list(map(int,input().split()))

s.sort() #오름차순 정렬

#변수 설정
count=0 #물 새는 곳을 막은 테이프의 개수 변수
i=0 #테이프로 막은 물 새는 곳의 개수 변수

while i<n: #물 새는 곳을 다 막을 때까지 반복
    count+=1
    start=s[i] #테이프로 물 다 막으면 다른 물 새는 곳을 start로 지정
    while i<n and s[i]<=start+l-1: #테이프의 한정된 길이l까지 반복
        i+=1
print(count)