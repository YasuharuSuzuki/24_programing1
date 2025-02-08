all_color = {'赤','白','黄','桃'}
input_set1 = set(input().split())

if len(input_set1) == 1:
    print( f"全部{input_set1.pop()}！")
elif len(input_set1) == 4:
    print("きれいだなぁ～")
else:
    print('{}がほしいなぁ～'.format("と".join(all_color - input_set1)))

