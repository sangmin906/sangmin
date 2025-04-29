#파라메트릭 서치로 풀기
#x,y,z설정
x,y=map(int,input().split())
z=int((y*100)/x)

#변수 설정
z_change=z
output=-1
low=1
high=1000000000

if z>=99: #승률 변하지 않을 때
    print(output)
else:
    while low<=high: #이분탐색
        mid=(low+high)//2
        x1=x+mid #반복문 안에 새로운 승률을 계산하기 위한 새로운 변수 설정
        y1=y+mid
        z_change=int((y1*100)/x1)
        if z<z_change: #기존 승률보다 클 때
            output=mid #현재 값 저장
            high=mid-1 #가장 낮은 값이 나올 때까지 반복
        else: #기존 승률과 같을 때
            low=mid+1
    print(output)