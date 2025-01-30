# 入力を受け取る
D = int(input())
K = input()
A = input()

# 左右の傾きを管理する変数
tilt = 0  # 正: 右傾き、負: 左傾き

# 1文字ずつ処理
time = 0  # debug用
for action, air in zip(K,A):
    # キー入力
    match action:
        case 'L':  tilt -= 1
        case 'R':  tilt += 1
    
    # キー入力
    match air:
        case 'L':  tilt -= 1
        case 'R':  tilt += 1
    
    # 傾きチェック
    if abs(tilt) > 3:
        print("YOU LOST")
        #print(f"YOU LOST, tilt={tilt}, time={time}")  # debug用
        break

    time += 1  # debug用
else:
    # breakせずに最後まで到達できた場合
    print("GOAL")
    #print(f"GOAL tilt={tilt}")  # debug用