#입력
n,m=map(int,input().split())

#책이 없는 경우
if n==0:
    print(0) #박스 0개

#책이 있는 경우
else:
    weight=list(map(int,input().split())) #각 책의 무게 입력
    sum=0 #박스에 넣을 책의 무게 합
    box_num=1 #박스의 개수
    for i in weight:
        if sum==m: #박스에 넣을 책 무게 합이 최대 넣을 수 있는 무게인 경우
            box_num+=1 #박스 추가
            sum=0
        elif sum+i>m: #박스에 넣을 책 무게 합이 최대 넣을 수 있는 무게를 초과한 경우
            box_num+=1 #박스 추가
            sum=0
        sum+=i #박스에 넣은 책 무게 더하기
    if sum==0: #박스에 딱 맞게 다 넣은 경우
        print(box_num-1) #의미없이 추가된 박스개수 제거
    else:
        print(box_num)