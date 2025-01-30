coler = input().split()

if len(set(coler)) == 1:
    print(f"全部{coler[0]}！")
elif len(set(coler)) == 5:
    print("キレイだなぁ〜")
else:
    coler_test = ["赤","白","黄","桃","紫"]
    coler_no = list(set(coler_test) - set(coler))
    if len(coler_no) == 1:
        print(f"{coler_no[0]}が欲しいなぁ〜")
    elif len(coler_no) == 2:
        print(f"{coler_no[0]}と{coler_no[1]}が欲しいなぁ〜")
    elif len(coler_no) == 3:
        print(f"{coler_no[0]}と{coler_no[1]}と{coler_no[2]}が欲しいなぁ〜")
