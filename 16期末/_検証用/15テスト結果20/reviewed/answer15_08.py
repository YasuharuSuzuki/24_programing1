score = list(map(int,input().split()))

score.sort(reverse=True)

for i in range(3):
    print(score[i])

