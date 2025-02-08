# 入力を受け取る
scores = list(map(int, input().split()))

# スコアを降順にソート
sorted_scores = sorted(scores, reverse=True)

# 上位3つのスコアを出力
for i in range(3):
    print(sorted_scores[i])