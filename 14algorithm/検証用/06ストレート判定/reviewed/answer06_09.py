C = input().split()

card_values = []
for card in C:
    C = card[1:]
    match C:
        case 'J': card = 11
        case 'Q': card = 12
        case 'K': card = 13
        case 'A': card = 1
        case _: card = int(C)
    card_values.append(card)

max_value = max(card_values)
min_value = min(card_values)

if max_value - min_value == 4:
    print("YES")
else:
    print("NO")