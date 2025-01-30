
all = {"赤","白","黄","桃","紫"}
s = set(input().split())

if len(s) == 1:
    print(f"全部{s.pop()}！")
elif len(s) >= 5:
    print(f"キレイだなぁ～")
elif len(s) == 4:
    print("{}が欲しいなぁ".format(list(all - s)[0]))
elif len(s) == 3:
    print("{}と".format(list(all - s)[1]) + "{}が欲しいなぁ".format(list(all - s)[0]))
else:
    print("{}と".format(list(all - s)[1]) + "{}と".format(list(all - s)[0]) + "{}が欲しいなぁ".format(list(all - s)[2]))
