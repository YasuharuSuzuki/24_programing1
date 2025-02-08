# 標準入力から便の種類と座席クラスを受け取る
flight_type, seat_class = input().split()

# dictを使って解決する場合
flight_prices = {'プレミアム便':40000,'通常便':30000,'深夜便':20000}
sheet_prices = {'ファーストクラス':2.5,'ビジネスクラス':1.5,'エコノミークラス':1.0}
price = int(flight_prices[flight_type]*sheet_prices[seat_class])

# 結果を出力
print(int(price))