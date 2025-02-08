all_color = {"赤","白","黄","桃"}

input_color = input().split()

if len(set(input_color)) == 1:
    print(f"全部{input_color.pop()}！")
elif len(set(input_color)) == 4:
    print("キレイだなぁ～")
else:
    print("{}が欲しいなぁ～".format("と".join(all_color - set(input_color))))
