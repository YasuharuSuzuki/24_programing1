Y = list(map(int,input().split()))
Y = sorted(Y,reverse = True)
A = Y[0] - Y[1]
B = A * 365
C = B % 4
D = B % 100
E = B % 400
F = C - D + E
print(f"{B} + {F}")

