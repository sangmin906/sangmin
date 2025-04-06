n=list(input())
capital=[]
dict={'a':'A','b':'B','c':'C','d':'D','e':'E','f':'F','g':'G','h':'H','i':'I','j':'J','k':'K','l':'L','m':'M','n':'N','o':'O','p':'P','q':'Q','r':'R','s':'S','t':'T','u':'U','v':'V','w':'W','x':'X','y':'Y','z':'Z'}
for i in n:
    if i in dict:
        capital.append(dict[i])
    else:
        capital.append(i)
for j in range(len(capital)):
#이후 쿠키의 신체측정도 포함하여 좀 더 수정해야함