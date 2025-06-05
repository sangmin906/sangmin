from bisect import bisect_left

#입력
l=int(input())
s=list(map(int,input().split()))
n=int(input())

if n in s: #n이 집합s 안의 원소일 때
    print(0)
else: #n이 집합s 안의 원소가 아닐 때
    s_sort=sorted(s) #집합s 배열
    sum=0
    if n<s_sort[0]: #n이 집합s의 모든 원소보다 작을 때
        left=1
        right=s_sort[0]-1

    else: #n의 크기가 집합s의 원소들 사이일 때(집합s의 모든 원소보다 작을 때)
        left=s_sort[bisect_left(s_sort,n)-1]+1 #n보다 작은 원소 중 가장 큰 원소 구하기
        right=s_sort[bisect_left(s_sort,n)]-1 #n보다 큰 원소 중 가장 작은 원소 구하기
    
    for A in range(left,right): #구간 [A,B] 중 A를 담당
        for B in range(left+1,right+1): #구간 [A,B] 중 B를 담당
            if n>=A and n<=B and A<B: #좋은 구간의 조건을 만족할 때(구간 [A,B]에서 A<=n<=B이고 A<B라는 조건을 만족할 때)
                sum+=1
    print(sum)