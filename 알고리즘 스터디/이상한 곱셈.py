#문자로 입력
a,b=input().split()

#변수 설정
sum=0

#새로운 곱셈 방법
for i in a:
    for j in b:
        sum+=int(i)*int(j) #문자인 i와 j를 정수로 변환해 계산

#출력
print(sum)