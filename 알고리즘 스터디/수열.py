#입력
n,k=map(int,input().split())
t=list(map(int,input().split()))

#변수 설정
start=0 #온도t에서 더하기 시작할 위치 변수
end=k-1 #온도t에서 더하기를 끝낼 위치 변수
output=sum(t[start:end+1]) #출력할 변수(미리 처음 온도의 합 넣어놓기)
sum=output #현재 온도의 합 변수(output과 비교)

for i in range(n-k):
    start+=1;end+=1 #현재의 시작과 끝 위치에서 1씩 더하기
    sum=sum-t[start-1]+t[end] #이전 온도의 합에서 start이전 위치의 온도는 빼고 새로 추가된 end 위치의 온도 더하기
    if output<sum: #이전에 가장 높았던 온도의 합보다 현재 온도의 합이 더 큰 경우
        output=sum

#출력
print(output)