n=int(input())
space=[]*n
count=0
check=False
waist=0
for i in range(n):
    space.append(list(input()))
for j in range(n):
    for k in range(n):
        if space[j][k]=="*" and not check:
            heart=[j+2,k+1]
            print(*heart)
            check=True
for l in range(heart[1]-2,-1,-1): #왼팔
    if space[heart[0]-1][l]=="*":
        count+=1
print(count,end=" ")
count=0
for l in range(heart[1],n): #오른팔
    if space[heart[0]-1][l]=="*":
        count+=1
print(count,end=" ")
count=0
for l in range(heart[0],n): #허리
    if space[l][heart[1]-1]=="*":
        count+=1
print(count,end=" ")
waist=count
count=0
for l in range(heart[0]+waist,n): #왼쪽 다리
    if space[l][heart[1]-2]=="*":
        count+=1
print(count,end=" ")
count=0
for l in range(heart[0]+waist,n): #오른쪽 다리
    if space[l][heart[1]]=="*":
        count+=1
print(count)