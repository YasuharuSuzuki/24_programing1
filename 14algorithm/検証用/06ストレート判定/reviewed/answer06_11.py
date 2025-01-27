def is_straight(cards):
    card_values = []
    for card in cards:
        value_str = card[1:]
        if value_str == 'J':
            value = 11
        elif value_str == 'Q':
            value = 12
        elif value_str == 'K':
            value = 13
        elif value_str == 'A':
            value = 1
        else:
            value = int(value_str)
        card_values.append(value)
    card_values.sort()
    for i in range(1, 5):
        if card_values[i] - card_values[i - 1] != 1:
            return "NO"
    return "YES"
cards_input = input().split()
result = is_straight(cards_input)
print(result)