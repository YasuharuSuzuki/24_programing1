
all = {"赤", "白", "黄", "桃"}
katta = set(input().split())

if len(katta) == 1:
    print(f"全部{katta.pop()}!")
elif len(katta) == 4:
    print("キレイだなぁ～")
elif len(katta) == 3:
    print("{}が欲しいなぁ～".format(list(all - katta)[0]))
else:
    print("{}と".format(list(all - katta)[0]) + "{}が欲しいなぁ～".format(list(all - katta)[1]))


