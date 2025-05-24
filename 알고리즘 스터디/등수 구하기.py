#입력
n,new,p=map(int,input().split())

#랭킹 리스트의 개수가 없는 경우
if n==0:
    print(1)

#랭킹 리스트의 개수가 있는 경우(이분탐색)
else:
    point=list(map(int,input().split())) #랭킹 리스트 입력
    point.sort(reverse=True) #내림차순으로 정렬
    low=0
    high=n-1
    output=-2 #등수를 출력하기 위한 변수로, mid값과 new값이 같지 않을 때를 고려해서 이분탐색에서 나오지 않을 -2라는 임의의 값 설정
    while low<=high:
        mid=(high+low)//2
        if point[mid]==new: #new값이 랭킹 리스트 안에 포함되어 있을 때(2가지의 경우로 나눔)
            if n==p and new==point[-1]: #랭킹 리스트의 갯수n와 리스트에 올라갈 수 있는 점수의 개수p가 같고, new값이 랭킹 리스트 끝순위와 같을 때(new값이 랭킹 리스트에 오르지 못할 때)
                output=-1
                print(output)
                break
            else: #랭킹 리스트에 새로운 등수로 오를 수 있을 때
                output=mid+1 #현재 mid값 저장
                high=mid-1 #현재 mid값과 같지만 가장 왼쪽에 있는 값을 찾기 위해 다시 이분탐색 시도
        elif point[mid]>new:
            low=mid+1
        else:
            high=mid-1

    #이분탐색 후
    if output==-2: #new값과 같은 값이 랭킹 리스트point 안에 없을 경우
        if low<=p-1: #low>high인 상태에서, 랭킹 리스트 안에 들 수 있는 경우(이분탐색으로 인해 low와 high의 사이엔 new값이 들어감)
            print(low+1)
        else: #low>high인 상태에서, 랭킹 리스트 안에 들 수 없는 경우
            print(-1)
    if output!=-2 and output!=-1:
        print(output) #22~24줄에서 이분탐색으로 찾은 가장 왼쪽에 있는 값의 위치 출력