Y = int(input())

Y=Y+1

if Y%4 == 0:#うるう年
    if Y%100 == 0:#うるう年ではない
        if Y%400 == 0:#うるう年
            print("4月5日")
        else:#うるう年ではない
            print("4月4日")
    else:#うるう年
        print("4月5日")
else:#うるう年ではない
    print("4月4日")

