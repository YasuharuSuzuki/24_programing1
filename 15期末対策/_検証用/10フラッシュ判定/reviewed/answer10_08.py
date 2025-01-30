cards = input().split()
numbers = []
for card in cards:
    num = card[:1]

numbers = list(set(numbers))

if len(num) == 1:
    print("YES")
else:
   print("NO")

