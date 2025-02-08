# 入力を受け取る
distance, total_time = map(int,input().split())
keys = input()
airs = input()

# 左右の傾きを管理する変数
tilt = 0  # 正: 右傾き、負: 左傾き
time = 0
pos = 0

# 1文字ずつ処理
for time in range(total_time):
    pos += 1
    sign = tilt//abs(tilt) if tilt!=0 else 0
    key = keys[time]
    air = airs[time]

    # キー入力
    match key:
        case 'L':
            tilt -= 1
        case 'R':
            tilt += 1
        case 'U':
            tilt += sign
            pos += 1
        case 'D':
            tilt -= sign
            pos -= 1
    
    # 風
    match air:
        case 'L':
            tilt -= 1
        case 'R':
            tilt += 1
        case 'H':
            pos -= 1
        case 'T':
            pos += 1

    pos = max(0,pos)

    # 傾きチェック
    if abs(tilt) > 3:
        print("YOU LOST")
        break
else:
    # breakせずに最後まで到達できた場合
    print("GOAL")