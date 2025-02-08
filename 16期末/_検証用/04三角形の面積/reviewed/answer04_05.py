import math
B, H = map(int,input().split())
R = B * H / 2
R_1 = math.floor(R*100)/100
print(f'{B} x {H} ÷ 2 = {R_1}')
print(f'こたえは{R_1}cm^2です')