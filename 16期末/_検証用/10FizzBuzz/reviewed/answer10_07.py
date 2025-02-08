f,l=map(int,input().split())

q_10=f
for q_10 in range(l):
    if (q_10+1)%3==0:
        if (q_10+1)%5==0:
            print("FizzBuzz", end=" ")
        else:
            print("Fizz",end=" ")
    elif (q_10+1)%5==0:
        print("Buzz",end=" ")
    else:
        print(q_10+1,end=" ")
