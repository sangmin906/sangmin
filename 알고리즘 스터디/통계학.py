#모듈 설정(여기서 쓰이지 않음)
from collections import defaultdict

#입력
n=int(input())
N=[int(input()) for i in range(n)]

#변수 설정
N_list=sorted(N)
N_dict={}
answer = []

mean=round(sum(N)/n) #산술평균
median=N_list[n//2] #중앙값

#최빈값
for i in N: #입력받은 N을 딕셔너리에 저장
    if i in N_dict:
        N_dict[i]+=1
    else:
        N_dict[i]=1

maxval = max(N_dict.values()) #딕셔너리 가장 큰 value값 저장
for k,v in N_dict.items(): #딕셔너리의 key값과 value값 순회
    if v == maxval:
        answer.append(k) #answer라는 리스트에 key값 저장

if len(answer)>=2: #maxval값이 중복인 경우
    answer=sorted(answer)
    answer=answer[1] #두번째로 작은 key값을 저장
else: #하나밖에 없다면
    answer=answer[0] #원래 있던 수 저장

#범위
range=max(N)-min(N)

#출력
print(f"{mean}\n{median}\n{answer}\n{range}")