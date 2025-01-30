kyori = int(input())
atai = input()
kaze = input()

# 1文字ずつ処理
for action in atai:
    # キー入力
    match action:
        case 'L':  kyori -= 1
        case 'L': kaze -= 1
        case 'R':  kyori += 1
        case 'R': kaze += 1
    # 傾きチェック
    if abs(kyori) > 3:
        print("YOU LOST")
        break
else:
    # breakせずに最後まで到達できた場合
    print("GOAL")