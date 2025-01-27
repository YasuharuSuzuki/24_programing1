N = int(input())
all_color = {'赤','白','黄','紫'}
input_set1 = set(input().split())

if len(input_set1) == 1:
    print(f"全部{input_set1.pop()}！")
elif len(input_set1) == 4:
    print("キレイだなぁ〜")
elif len(all_color - input_set1) == 2:
    print("{}と{}が欲しいなぁ〜".format(list(all_color - input_set1)[0],list(all_color - input_set1)[1]))
else:
    print("{}が欲しいなぁ〜".format(list(all_color - input_set1)[0]))