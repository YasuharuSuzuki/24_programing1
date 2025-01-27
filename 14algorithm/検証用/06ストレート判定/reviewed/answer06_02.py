C = list(input().split())
sutonashi = []
for i in C:
    if "J" in i:
        sutonashi.append(11)
    elif "Q" in i:
        sutonashi.append(12)
    elif "K" in i:
        sutonashi.append(13)
    elif "A" in i:
        sutonashi.append(1)
    else:
        sutonashi.append(int(i[1:]))
sutonashi.sort()
if sutonashi == list(range(sutonashi[0],sutonashi[0]+5)):
    print("YES")
else:
    print("NO")