cards = input().split()
number = []
for card in cards:
    num = card[1:]
    match num:
        case 'J':
            number.append(11)
        case 'Q':
            number.append(12)
        case 'K':
            number.append(13)
        case 'A':
            number.append(1)
        case _:
            number.append(int(num))
numbers = list(set(number))
if max(numbers) - min(numbers) == 4 and len(numbers) == 5:
    print("YES")
else:
    print("NO")