t=int(input()) #테스트케이스
for i in range(t):
    n,s=map(str,input().split()) #숫자, 문자열 입력
    n=int(n) #n을 정수로 변환
    for j in s: #각 문자열 j에 대하여
        print(j*n,end="") #j를 n번 반복
    print() #다음줄 넘어가기