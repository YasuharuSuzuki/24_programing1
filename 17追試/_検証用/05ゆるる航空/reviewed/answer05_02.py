# 標準入力から便の種類と座席クラスを受け取る
flight_type, seat_class = input().split()

# 便の種類による基本料金の設定
if flight_type == "プレミアム便":
    price=40000
elif flight_type == "通常便":
    price=30000
else:
    price=20000

# 座席クラスによる倍率の適用
if seat_class == "ファーストクラス":
    price*=2.5
elif seat_class == "ビジネスクラス":
    price*=1.5

# 結果を出力
print(int(price))