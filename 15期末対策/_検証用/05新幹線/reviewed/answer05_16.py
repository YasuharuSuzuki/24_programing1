n = input()

cost = [10000,9000,8000]

if "のぞみ" in n:
    cost = 10000
elif "ひかり" in n:
    cost = 9000
elif "こだま" in n:
    cost = 8000

if "自由席" in n:
    cost -= 500
elif "グリーン車" in n:
    cost += 5000

print(cost)
