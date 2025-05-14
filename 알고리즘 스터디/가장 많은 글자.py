#변수 설정
n=1
a_dict={}

#입력 및 가공
while n<=50:
    try:
        a=input()
        a=list(a.replace(" ","")) #공백 제거
        for i in a: #리스트에서 딕셔너리로 옮기기{알파벳:알파벳 개수}
            if i in a_dict: #딕셔너리에 이미 존재하는 알파벳일 때
                a_dict[i]+=1 #개수 추가
            else: #딕셔너리에 존재하지 않는 알파벳일 때
                a_dict[i]=1 #키,값 추가
        n+=1
    except EOFError: #주어진 입력이 끝나도 계속 입력받으려 할 때 생기는 오류
        break #예외처리하여 벗어나기
a_list="".join(sorted([k for k,v in a_dict.items() if v==max(a_dict.values())])) #딕셔너리에서 가장 큰 값을 가진 키들을 순서대로 공백없이 새로운 리스트에 저장
print(a_list) #출력