q9=int(input())

if (q9+1)%4==0:
    if (q9+1)%100==0:
        if (q9+1)%400==0:
            print("4月5日")
        else:
            print("4月4日")
    else:
        print("4月5日")
else:
    print("4月4日")