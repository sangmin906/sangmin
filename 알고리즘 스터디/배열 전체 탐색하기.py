#모듈 설정
from bisect import bisect_left, bisect_right

#입력
n,m=map(int,input().split())
a=sorted(list(map(int,input().split())))

#질의에 따른 유형 나누기
for i in range(m):
    b=list(map(int,input().split())) #질의가 저장된 배열b 입력
    if b[0]==1:
        print(n-bisect_left(a,b[1]))
    elif b[0]==2:
        print(n-bisect_right(a,b[1]))
    elif b[0]==3:
        print(bisect_right(a,b[2])-bisect_left(a,b[1]))

#참고
#bisect_left(특정 리스트,특정 숫자): (정렬된 자료)특정 리스트 안에 나열되어 있는 특정 숫자의 가장 왼쪽 인덱스
#bisect_right(특정 리스트,특정 숫자): (정렬된 자료)특정 리스트 안에 나열되어 있는 특정 숫자 다음으로 오는 숫자의 가장 왼쪽 인덱스