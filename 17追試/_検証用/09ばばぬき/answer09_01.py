# 6人分の手札を入力
hands = []
for i in range(6):
    hand = input().split()
    hands.append(hand)

# 結果を格納するリスト
pair_results = []

# 各プレイヤーのペアとジョーカーを判定
joker_player = 0
for i in range(6):
    # ジョーカー判定
    if '☆' in hands[i]:
        joker_player = i + 1
        hands[i].remove('☆')
    
    # ペア判定用のリスト
    ranks = []
    for card in hands[i]:
        ranks.append(card[1:])  # スートを除いたランク部分を追加
    
    # ペア判定
    has_pair = False
    for rank in ranks:
        if ranks.count(rank) >= 2:
            has_pair = True
            break
    
    # 結果を追加
    if has_pair:
        pair_results.append("Yes")
    else:
        pair_results.append("No")

# 結果を出力
print(" ".join(pair_results))
print(joker_player)