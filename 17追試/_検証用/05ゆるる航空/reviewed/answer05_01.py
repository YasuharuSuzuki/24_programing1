# 標準入力から便の種類と座席クラスを受け取る
flight_type, seat_class = input().split()

# 便の種類による基本料金の設定
match flight_type:
    case "プレミアム便": price=40000
    case "通常便": price=30000
    case "深夜便": price=20000

# 座席クラスによる倍率の適用
match seat_class:
    case "ファーストクラス": price*=2.5
    case "ビジネスクラス": price*=1.5

# 結果を出力
print(int(price))