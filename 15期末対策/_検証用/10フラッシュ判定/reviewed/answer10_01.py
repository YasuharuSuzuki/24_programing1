# 入力を受け取る
cards = input().split()

# 絵柄（スート）部分をsetで取り出す
suits = set([card[:1] for card in cards])

# フラッシュの判定
if len(suits) == 1:
    print("YES")
else:
    print("NO")