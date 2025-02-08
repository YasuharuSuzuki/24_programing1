Ys,Ye = map(int,input().split())

YsYe = abs(Ys - (1 +Ye))

if (Ys % 4 == 0) and (Ys % 100 != 0 or Ys & 400 == 0):
    print((YsYe * 365 + (YsYe // 4) - (YsYe // 100) + (YsYe // 400))+1)
elif (Ys % 100 == 0) and (Ys % 400 == 0):
    print((YsYe * 365 + (YsYe // 4) - (YsYe // 100) + (YsYe // 400))+1)
else:
    print((YsYe * 365 + (YsYe // 4) - (YsYe // 100) + (YsYe // 400)))



