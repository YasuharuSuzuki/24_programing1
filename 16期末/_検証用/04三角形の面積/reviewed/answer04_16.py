teihen, high = map(int, input(). split())

menseki = teihen * high / 2
menseki = round(menseki,1)
menseki = ('{:.01f}'.format(menseki))

print(f"{teihen} x {high} ÷ 2 = {menseki}")
print(f"こたえは {menseki} cm^2です")


