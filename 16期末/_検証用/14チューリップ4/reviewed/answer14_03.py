colors={"赤","白","黄","桃"}
input_color=set(input().split())
if len(input_color)==1:
    print(f"全部{input_color.pop()}！")
elif len(input_color)==4:
    print("キレイだなぁ〜")
else:
    print("{}が欲しいなぁ〜".format("と".join(list(colors-input_color))))