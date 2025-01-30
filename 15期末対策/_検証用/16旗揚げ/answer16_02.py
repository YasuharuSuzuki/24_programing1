a = list(input().split())
b = list(input().split())
siro = 0
aka = 0
c = a + b
siro = c.count("白下げない")
siro -= c.count("白げ下げて")
siro -= c.count("白げ上げない")
siro += c.count("白げ上げて")

aka = c.count("赤下げない")
aka -= c.count("赤下げて")
aka -= c.count("赤上げない")
aka += c.count("赤下げて")

if aka >= 1 and siro >= 1:
    print("赤　白")
elif aka >= 1:
    print("赤")
elif siro >= 1:
    print("白")
else:
    print("どちらも上げない")