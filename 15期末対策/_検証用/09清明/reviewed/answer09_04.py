Y = int(input())
Y1 = (Y+1) / 4
if (Y+1) % 4 == 0:
    if Y1 % 100 == 0:
        print("4月5日")
    elif Y1 % 5 == 0:
        print("4月4日")
    else:
        print("4月5日")
else:
    print("4月4日")