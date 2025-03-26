number=int(input())
n=list(map(int,input()))
sum=n[0]
for i in range(number):
    if i+1<number:
        sum=n[i+1]+sum
print(sum)