P = list(map(int, input().split()))

P.sort(reverse=True)

# 上位5名の点数を出力
for i in P[:3]:
    print(i)



