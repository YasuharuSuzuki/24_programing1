all_color = {'赤', '白', '黄', '紫'}

# チューリップの購入数を入力
N = int(input())
# 購入したチューリップの色を入力
input_set1 = set(input(ム).split())

# 色の種類の数を確認
if len(input_set1) == 1:
    print(f'全部{input_set1.pop()}！')
elif len(input_set1) == 4:
    print('キレイだなぁ〜')
else:
    # 購入していない色をリストアップ
    missing_colors = list(all_color - input_set1)
    if len(missing_colors) > 1:
        print('と'.join(missing_colors[:-1]) + 'と' + missing_colors[-1] + 'が欲しいなぁ〜')
    else:
        print(f'{missing_colors[0]}が欲しいなぁ〜')