#입력
n=list(input().split('-'))

#변수 설정
compute=[] #-인 연산자와 연관된 계산을 하기 위한 리스트
m=[] #+인 연산자와 연관된 계산을 하기 위한 리스트

#숫자 전처리
for j in range(len(n)):
    m=n[j].split('+') #+인 연산자를 기준으로 리스트 m에 저장
    for k in range(len(m)):
        m[k]=str(int(m[k])) #숫자 첫번째자리가 0으로 시작하는 숫자를 일반 숫자로 변경
    m=str(eval('+'.join(m))) #나누어진 숫자들을 다시 +로 연결시켜 계산 후 문자로 변경
    n[j]=m #다시 n에 저장

for i in range(len(n)):
    compute.append(n[i]) #리스트 compute에 리스트 n을 옮기기
    if i!=len(n)-1: #옮기는 과정에서 숫자 사이마다 -추가(마지막 숫자 끝에는 제외)
        compute.append('-')
compute=''.join(compute) #리스트 문자로 변경
compute=eval(compute) #-로 이어진 문자로 된 숫자를 계산

#출력
print(compute)