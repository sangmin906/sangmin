n,m=map(int,input().split())
basket=[0]*n
for a in range(m):
    i,j,k=map(int,input().split())
    for b in range(i-1,j):
        basket[b]=k
print(*basket)
# *은 언패킹(unpacking)연산자-리스트의 요소를 공백을 구분자로 나열하여 출력
# " ".join(map(str, basket))을 통해 리스트 숫자를 문자열로 변환 후 공백으로 구분하여 출력