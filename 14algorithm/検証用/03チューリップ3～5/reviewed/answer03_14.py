colors = {"赤","黄","紫","白"}
N= input()
C= set(input().split())
if len(C) == 1:
    print(f'全部{C.pop()}！')
elif len(C) == 4:
    print('キレイだなぁ〜')
elif len(C)==2:
   print('{}と{}が欲しいなぁ～'.format(list(colors-C)[0],list(colors-C)[1]))
else:
    print('{}が欲しいなぁ'.format(list(colors - C)[0]))