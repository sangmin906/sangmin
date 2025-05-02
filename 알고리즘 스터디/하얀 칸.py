chessboard=[input() for i in range(8)]
num=0
line=0
while line<=7:
    if line%2==0:
        for k in range(4):
            if chessboard[line][k*2]=='F':
                num+=1
    else:
        for l in range(4):
            if chessboard[line][(l*2)+1]=='F':
                num+=1
    line+=1
print(num)