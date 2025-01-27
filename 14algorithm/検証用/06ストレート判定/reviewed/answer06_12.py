def solve():
    cards = input().split()
    ranks = []

    for card in cards:
        rank = card[1:]

        if rank == 'J':
            rank = 11
        elif rank == 'Q':
            rank = 12
        elif rank == 'K':
            rank = 13
        elif rank == 'A':
            rank = 1
        else:
            rank = int(rank)

        ranks.append(rank)

    ranks.sort()

    is_straight = True
    for i in range(1, len(ranks)):
        if ranks[i] != ranks[i - 1] + 1:
            is_straight = False
            break

    if is_straight:
        print("YES")
    else:
        print("NO")

solve()


