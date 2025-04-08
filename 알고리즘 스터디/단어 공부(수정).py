n=input().upper()
count={} #각 알파벳 수 넣을 딕셔너리
for i in n: #각 알파벳 수 체크
    if i in count:
        count[i]+=1
    else:
        count[i]=1
lot=max(count.values()) #가장 많이 사용된 알파벳의 개수
overlap=[]
for j in count: #겹치는지 확인
    if count[j]==lot:
        overlap.append(j)
if len(overlap)>1:
    print("?")
else:
    print(overlap[0])