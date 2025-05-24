#입력
n=[int(input()) for i in range(10)]

#변수 설정
sum=0

#n에 있는 점수 차례로 더하기
for i in range(11): #10점*10일 때 출력이 안 되는 상황을 방지하고자 0~10까지 설정
    if sum==100:
        print(100)
        break
    elif sum>100: #sum이 100 이상이기 시작할 때와 100을 넘지 않던 그 이전이 같을 때 비교하기
        if sum-100==100-(sum-n[i-1]): #같을 때
            print(sum) #현재 sum이 100 이상인 값 출력
            break
        elif sum-100>100-(sum-n[i-1]): #현재 sum이 100에서 더 멀 때
            print(sum-n[i-1]) #이전 sum 출력
            break
        else: #현재 sum이 100에서 가까울 때
            print(sum) #현재 sum 출력
            break
    if i==10: #구하는 범위는 0~9까지이기에, i=10인 경우는 더하지 않고 루프 빠져나오기
        break
    sum+=n[i]
if sum<100: #모든 점수를 더해도 100이하인 경우
    print(sum)