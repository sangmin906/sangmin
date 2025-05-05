import sys
input = sys.stdin.readline

#변수 입력
m=int(input())
s=set()
for i in range(m):
    order=list(input().split())
    #추가
    if order[0]=='add':
        s.add(int(order[1]))
    #제거
    elif order[0]=='remove':
        s.discard(int(order[1]))
    #체크해서 있으면 1, 없으면 0 출력
    elif order[0]=='check':
        if int(order[1]) in s:
            print(1)
        else:
            print(0)
    #있으면 제거, 없으면 추가
    elif order[0]=='toggle':
        if int(order[1]) in s:
            s.remove(int(order[1]))
        else:
            s.add(int(order[1]))
    #범위 내의 전체집합으로 변경
    elif order[0]=='all':
        s={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    #공집합으로 변경
    elif order[0]=='empty':
        s=set()