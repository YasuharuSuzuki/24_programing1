Y = input()
Y = int(Y)
if Y%4 == 3 and Y%100 == 99 and Y%400 == 399:
    print("4月5日")
elif Y%4 ==3 and Y%100 == 99:
    print("4月4日")
elif Y%4 == 3:
    print("4月5日")
else:
    print("4月4日")
