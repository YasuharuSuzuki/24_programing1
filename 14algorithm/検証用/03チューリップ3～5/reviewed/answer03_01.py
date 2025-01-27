colors={"赤","白","黄","紫"}
N=int(input())
C=set(input().split())
len_set=len(C)
dif_list=list(colors-C)
if len_set==1:
    print(f"全部{list(C)[0]}！")
elif len_set==2:
    print(f"{dif_list[0]}と{dif_list[1]}が欲しいなぁ〜")
elif len_set==3:
    print(f"{dif_list[0]}が欲しいなぁ〜")
else:
    print("キレイだなぁ〜")