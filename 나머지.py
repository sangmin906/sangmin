a=[int(input()) for i in range(10)]
#입력받는 함수 한줄로 만들어보기(리스트 컴프리헨션)
for j in range(10):
    a[j]=a[j]%42 #set()로 리스트에서 중복 제거
print(len(set(a)))