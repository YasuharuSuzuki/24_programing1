N,S,E = map(int, input().split())
P = list(map(int, input().split()))
A = sum((P[S-1:E]))
print(A)

