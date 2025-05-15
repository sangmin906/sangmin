#입력
x,y=input().split()

x=x[::-1] #Rev(x)
y=y[::-1] #Rev(y)
z=str(int(x)+int(y)) #Rev(x)+Rev(y)
z=z[::-1] #Rev(Rev(x)+Rev(y))

#앞에 0이 붙어있을 경우 0 제거
n=0
while int(z[n])==False: #z의 n번째 요소가 False(=0)인 경우에만 반복
    n+=1
z=z[n:] #0인 0~n-1번째를 제외하고, 0이 아닌 나머지 n번째 요소부터 출력(앞에 0이 없다면 0번째 요소부터 출력)

#출력
print(z)