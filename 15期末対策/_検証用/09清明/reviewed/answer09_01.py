# ここから解答例
# 入力
Y = int(input())

# 翌年がうるう年かどうかの判定
next_year = Y + 1
is_next_leap = (next_year % 4 == 0) and \
               (next_year % 100 != 0 or next_year % 400 == 0)

# 日付の判定
if is_next_leap:
    print("4月5日")
else:
    print("4月4日")
