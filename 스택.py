n=int(input())
stack=[]
for i in range(n):
    command=input().split()
    if command[0]=="push":
        stack.append(int(command[1]))
    elif command[0]=="pop":
        if not stack:
            print(-1)
        else:
            a=stack.pop()
            print(a)
    elif command[0]=="size":
        print(len(stack))
    elif command[0]=="empty":
        if not stack:
            print(1)
        else:
            print(0)
    elif command[0]=="top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])