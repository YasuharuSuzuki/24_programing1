n =input()
colors = set(input().split())

if len(colors) == 1:
    print(f"全部{list(colors)[0]}!")
elif len(colors) == 4:
    print("キレイだなぁ〜")
else:
    missing = {"赤", "白", "黄", "紫"} - colors
    print(f"{'と'.join(missing)}が欲しいなぁ〜")