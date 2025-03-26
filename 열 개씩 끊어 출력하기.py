a=input() #굳이 리스트로 받지 않아도 가능
b=len(a) #len()-리스트나 문자열의 길이
for i in range(0,b,10):
    print(a[i:i+10])