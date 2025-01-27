all_color = {'赤','白','黃','紫',}
N = input()
input_set1 = set(input().split())
A = list(all_color-input_set1)
if len(input_set1) == 1:
    print(f'全部{input_set1.pop()}！')
elif len(input_set1) == 4:
    print('キレイだなぁ〜')
elif len(input_set1) == 3:
    print('{}が欲しいなぁ'.format(list(A))[0])
elif len(input_set1) == 2:
    print('{}と{}が欲しいなぁ'.format(list(A)[0],(list(A)[1])))
