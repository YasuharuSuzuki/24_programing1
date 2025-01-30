C = set(input().split())
all_color = {'赤','白','黄','桃','紫'}

if len(C) == 1:
    print(f"全部{C.pop()}！")
elif len(C) == 5:
    print("キレイだなぁ〜")
elif len(all_color - C) ==3:
    print("{}と{}と{}が欲しいなぁ〜".format(list(all_color - C)[0],list(all_color - C)[1],list(all_color - C)[2]))
elif len(all_color - C) == 2:
    print("{}と{}が欲しいなぁ〜".format(list(all_color - C)[0],list(all_color - C)[1]))
else:
    print("{}が欲しいなぁ〜".format(list(all_color - C)[0]))