y = int(input())

yy = y +1

if y % 4 == 0:
    print(f"4月4日")
elif y % 400 == 0:
    print(f"4月5日")
elif y % 100 == 0:
    print(f"4月4日")
else:
    if yy % 100 == 0:
        print(f"4月4日")
    else:
      print(f"4月5日")
