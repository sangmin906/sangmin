a=input()
b=input()
c=input()
n=["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
m=[1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]
x=n.index(a)*10+n.index(b)
y=m[n.index(c)]
print(x*y)