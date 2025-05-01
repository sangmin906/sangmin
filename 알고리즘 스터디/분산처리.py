import sys
input=sys.stdin.readline
#테스트케이스 입력
t=int(input())

for i in range(t):
    a,b=map(int,input().split())
    a=a%10 #a 일의 자리만 남기기
    #제곱해도 똑같은 수들은 따로 만들기
    if a==0:
        print(10)
    elif a==1:
        print(1)
    elif a==5:
        print(5)
    elif a==6:
        print(6)
    #제곱해서 다양한 경우가 나오는 수들 딕셔너리로 만들기
    else:
        cycles={
            2:[2,4,8,6],
            3:[3,9,7,1],
            4:[4,6],
            7:[7,9,3,1],
            8:[8,4,2,6],
            9:[9,1]
        }
        cycle=list(cycles[a]) #딕셔너리에서 a 가져오기
        print(cycle[(b-1)%len(cycle)]) #b에 의해 a의 다양한 경우 중 하나를 선택해 출력