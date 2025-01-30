Y = int(input())
D = 0
tosi = (Y + 1) % 4 #=0うるう年
tokubetu = (Y + 1) % 100 #特殊　うるうどしにならない
tokubetu2 = (Y + 1) % 400
if tokubetu == 0 and tokubetu2 > 0:
    D = 4
elif tosi == 0:
    D = 5
else:
    D = 4

print(f"4月{D}日")

