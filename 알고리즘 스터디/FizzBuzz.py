n=[input() for i in range(3)]
for j in range(3):
    if n[j].isdigit()==True:
        a=int(n[j])+(3-j)
        if a%15==0:
            print("FizzBuzz")
        elif a%5==0:
            print("Buzz")
        elif a%3==0:
            print("Fizz")
        else:
            print(a)
        break