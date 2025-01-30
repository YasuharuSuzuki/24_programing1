y = int(input())

if ((y + 1)%4) == 0:
    if ((y + 1)%100) == 0:
        print("4月4日")
    else:
        print("4月5日")
else:
    print("4月4日")