#입력
a=input()
b=input()

#변수 설정
n=0 #a의 범위 한정 역할(마우스 커서 같은 역할)
output=0 #출력할 값 입력

#a에서 b를 찾기
while n<=len(a)-len(b):
    if a[n:n+len(b)]==b: #a에서 b의 길이만큼의 문서가 b랑 동일할 경우
        output+=1 #찾은 개수 추가
        n+=len(b) #이미 찾은 문서를 제외하기 위해 b의 길이만큼 추가하여 범위 한정
    else: #동일하지 않을 경우
        n+=1 #a문서를 한 글자씩 옮기면서 범위 한정

#출력
print(output)