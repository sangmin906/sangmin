#입력
n,k=map(int,input().split())
a=list(map(int,input().split(',')))

#변수 설정
b=[]
sum=0

#k가 0일 때
if k==0:
    print(*a,sep=',') #쉼표를 구분자로 하여 언패킹으로 a출력

#k가 0이 아닐 때
else:
    for i in range(k): #k번 반복
        if i==0: #처음 시작할 때(i=0)
            for j in range(1,n):
                b.append(a[j]-a[j-1]) #a의 인접한 두 원소의 차이를 b에 저장
        else: #처음 시작이 아닐 때(i>0)
            for j in range(sum+1,sum+n-i): #수열 크기에 따른 계산할 범위 조정, b에 기존 값을 없애는 것이 아닌 추가하는 것이기에 올바른 범위를 계산하고자 sum 붙임
                b.append(b[j]-b[j-1]) #계산할 기존 b의 인접한 두 원소의 차이를 b에 추가
        if i>=1: #2번째 반복부터
            sum+=n-i #계산한 범위 추가(계산할 범위 조정에 필요)
    print(*b[-(n-k):],sep=',') #마지막으로 계산한 b에 있는 수열 출력, 쉼표를 구분자로 하여 언패킹으로 출력