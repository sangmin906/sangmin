#입력
s1,s2,s3=map(int,input().split())

#s1, s2, s3 각 리스트에 1~입력된 값으로 변환하여 저장
s1_list=list(range(1,s1+1))
s2_list=list(range(1,s2+1))
s3_list=list(range(1,s3+1))
sum_dict={}

#세 주사위의 합 경우를 계산
for i in s1_list:
    for j in s2_list:
        for k in s3_list:
            if i+j+k in sum_dict: #이미 합한 값이 저장되어 있는 경우
                sum_dict[i+j+k]+=1 #1 추가(개수 세기)
            else: #합한 값이 저장되어 있지 않은 경우
                sum_dict[i+j+k]=1 #새로운 합 추가하기

#가장 높은 빈도로 나오는 합을 출력하기
output=[key for key,value in sum_dict.items() if value==max(sum_dict.values())] #가장 큰 값과 관련된 키를 output에 저장
print(min(output)) #여러 키들 중 가장 작은 키 출력