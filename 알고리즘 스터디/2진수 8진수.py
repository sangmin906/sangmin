#올바른 버전
a_2=int(input(),2) #2진수 문자열을 10진수 정수로 변환
a_8=format(a_2,'o') #10진수 정수를 8진수문자열로 변환
print(a_8)

#풀어쓴 버전(시간초과)
# a=str(input()) #문자로 입력받기
# a_list=[]
# count=0

# if len(a)%3!=0: #입력받은 a가 3으로 나누어떨어지지 않는경우
#     a='0'*(3-(len(a)%3))+a #앞에 임의로 0 붙이기
# for i in range(len(a)//3): #3개씩 a_little_list에 담아 a_list에 담기
#     a_little_list=[]
#     for j in range(len(a)-1,len(a)-4,-1): #자릿수 때문에 거꾸로 담기
#         a_little_list.append(int(a[j-count]))
#     a_list.append(a_little_list)
#     count+=3

# output=0
# for k in range(len(a)//3): #위의 과정대로 리스트에 옮겨담은 후, 8진수 변환 시작
#     sum=0
#     for l in range(3): #3자리마다 8진수로 변환
#         sum+=(a_list[k][l])*(2**l)
#     output+=sum*(10**k) #변환한 각각의 8진수들을 합치기
# print(output)
