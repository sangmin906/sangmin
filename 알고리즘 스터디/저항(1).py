a=input()
b=input()
c=input()
#딕셔너리 선언
n={"black":[0,1],"brown":[1,10],"red":[2,100],"orange":[3,1000],"yellow":[4,10000],"green":[5,100000],"blue":[6,1000000],"violet":[7,10000000],"grey":[8,100000000],"white":[9,1000000000]}
x=n[a][0]*10+n[b][0]
y=n[c][1]
print(x*y)