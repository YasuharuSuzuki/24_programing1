# 入力
T, S = input().split()

# 基本料金を設定
train = 0
match T:
    case "のぞみ": train=10000
    case "ひかり": train=9000
    case "こだま": train=8000

# 座席区分による料金調整
sheet = 0
match S:
    case "自由席": sheet=-500
    case "グリーン車": sheet=+5000

# 出力
print(train+sheet)