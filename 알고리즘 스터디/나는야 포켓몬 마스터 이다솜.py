n,m=map(int,input().split())
N_key_num={} #숫자를 키로 저장
N_key_name={} #이름을 키로 저장
#외워야 할 것 입력
for i in range(n):
    name=str(input())
    N_key_num[str(i+1)]=name
    N_key_name[name]=str(i+1)
#문제 풀어야 할 것 입력
for j in range(m):
    M=str(input())
    if M.isdigit()==True: #입력받은 M값이 숫자라면
        print(N_key_num[M]) #숫자 key에 기반한 value(이름) 출력
    else:
        print(N_key_name[M]) #이름 key에 기반한 value(숫자) 출력