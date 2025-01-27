C = input().split()


# 数字部分を抽出して対応する値に変換
card_values = []
for card in C:
    if 'A' in card:
        card_values.append(1)
    elif 'J' in card:
        card_values.append(11)
    elif 'Q' in card:
        card_values.append(12)
    elif 'K' in card:
        card_values.append(13)
    else:
        card_values.append(int(card[1:]))

# 数字を昇順に並べる
card_values.sort()

# 連続しているかチェック
if card_values == list(range(card_values[0], card_values[0] + 5)):
    print("YES")
else:
    print("NO")


