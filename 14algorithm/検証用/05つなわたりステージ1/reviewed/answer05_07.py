# 入力を受け取る
S = input()

# 初期設定
position = 0  # 現在の位置
tilt = 0      # 傾き

# 文字列 S の各文字に対して処理を行う
for action in S:
    # 1秒間に1m進む
    position += 1

    # アクションに応じて傾きを変更
    if action == 'L':
        tilt += 1
    elif action == 'R':
        tilt -= 1
    elif action == 'N':
        pass  # 何もしない



    # 傾きが+3または-3を超えた場合、落ちる
    if (tilt > 3) or (tilt < -3):
        print("YOU LOST")
        break

if position >= 20:
        print("GOAL")


