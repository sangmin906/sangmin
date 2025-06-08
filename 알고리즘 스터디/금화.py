#t-단위 시간, x-금화 개수, m-몬스터수
#d-몬스터와의 거리, s-몬스터가 단위 시간 당 오는 거리
#행위-멈추기, 주워담기
#순서
# 1. 단위 시간동안 가장 빠르게 다가오는 몬스터를 타겟으로 잡기(각 몬스터마다 d/s를 해 가장 낮은 수의 몬스터가 타겟)
# 2. 타겟이 오기 직전까지 금화 모으기(현재 거리 변수에 단위 시간 당 오는 거리s를 더하면서 타겟과의 총거리d를 비교하여 파악)
# 3. 타겟이 가까이 왔다면 한 번 쉬어주기(현재 거리 변수에 타겟이 단위 시간 당 오는 거리s 빼기)
# 4. 타켓이 s만큼 멀어졌다면 다시 금화 모으기
# 5. 단위 시간t가 끝날 때까지 3-4를 반복
# 6. 단위 시간t가 끝났다면 총 모인 금화 개수 출력

t,x,m=map(int,input().split())
target=0
coin=0
distance=0
if m==0:
    print(t*x)
else:
    for i in range(m):
        d,s=map(int,input().split())
        if target==0 or target>=d/s:
            target=d/s
            d_t,s_t=d,s
    for j in range(t):
        if d_t==s_t:
            break
        distance+=s_t
        if distance<d_t:
            coin+=x
        else:
            distance-=s_t*2
    print(coin)
#어느 부분이 틀렸는지 모르겠음.