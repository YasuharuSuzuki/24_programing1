y = int(input())

if y % 400 == 0:
    print("4月4日")
elif y % 100 == 0:
    print("4月5日")
elif y % 4 == 0:
    print("4月4日")
else:
    print("4月5日")