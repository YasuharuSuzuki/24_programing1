iro=input().split()

iro_list={"赤","白","黄","桃","紫"}
iro_set=set(iro)

if len(iro_set) == 1:
    print(f"全部{iro[0]}！")
elif iro_set==iro_list:
    print("キレイだなぁ〜")
else:
    iro_none=list(iro_list-iro_set)
    if len(iro_none)==1:
        print(f"{iro_none[0]}が欲しいなぁ〜")
    elif len(iro_none)==2:
        print(f"{iro_none[0]}と{iro_none[1]}が欲しいなぁ〜")
    else:
        print(f"{iro_none[0]}と{iro_none[1]}と{iro_none[2]}が欲しいなぁ〜")