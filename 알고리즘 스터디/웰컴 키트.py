#입력
n=int(input())
size=list(map(int,input().split()))
t,p=map(int,input().split())

#티셔츠 주문 갯수 파악 및 출력
sum=0 #각 사이즈 당 주문할 갯수 합하기 위한 변수 설정
for i in range(6):
    if size[i]==0: #사이즈 갯수 0이라면 넘어가기
        continue
    elif size[i]%t==0: #사이즈 갯수가 t의 배수라면 그냥 나누기
        sum+=size[i]//t
    else:
        sum+=(size[i]//t)+1 #t로 나눈 후 +1
print(sum)
#펜 주문 갯수 출력
print(n//p,n%p)