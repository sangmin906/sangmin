#입력
n=list(input())

if len(n)==1: #한자리수라면(유진수X)
    print("NO")
else: #한자리가 아니라면
    for i in range(1,len(n)): #입력값을 2개로 분할하여 계산하기 위한 분할위치 제공
        left=1 #앞부분 자리수의 곱
        right=1 #뒷부분 자리수의 곱
        for j in n[:i]: #0부터 i까지 앞부분 자리수 곱하기
            left*=int(j) #입력받은 문자를 정수로 변경하여 계산
        for k in n[i:]: #i부터 끝까지 뒷부분 자리수 곱하기
            right*=int(k)
        if left==right: #곱들이 서로 같다면 YES출력/아니라면 다시 될 때까지 반복
            print("YES")
            break
    if left!=right: #입력값을 2개로 분할했을 때의 모든 곱의 경우를 계산하였음에도 나오지 않은 경우
        print("NO")