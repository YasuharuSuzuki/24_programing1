colors={"赤","白","黄","桃","紫"}
C=set(input().split())
ans=list(colors-C)
if len(C)==1:
    print(f"全部{list(C)[0]}!")
elif len(C)==5:
    print("キレイだなぁ〜")
elif len(C)==4:
    print(f"{ans[0]}が欲しいなぁ〜")
elif len(C)==3:
    print(f"{ans[0]}と{ans[1]}が欲しいなぁ〜")
else:
    print(f"{ans[0]}と{ans[1]}と{ans[2]}が欲しいなぁ〜")