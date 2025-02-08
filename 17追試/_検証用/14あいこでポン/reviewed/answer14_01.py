# 入力
first = input()
second = input()

# じゃんけんの手を集合で用意
hands = {"グー", "チョキ", "パー"}

# あいこになるパターン1: 全員同じ手
if first == second:
    print(first)
# あいこになるパターン2: 全員異なる手
else:
    # 使われていない手を求める
    used_hands = {first, second}
    remaining_hand = hands - used_hands
    print(list(remaining_hand)[0])