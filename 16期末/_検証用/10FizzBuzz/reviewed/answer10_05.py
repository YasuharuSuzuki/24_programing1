N, M = map(int,input().split())
D = list(range(N,M+1))
for i in range(M-N+1):
    if D[i] % 3 == 0 and D[i] % 5 == 0:
        D[i] = 'FizzBuzz'
    elif D[i] % 3 == 0:
        D[i] = 'Fizz'
    elif D[i] % 5 == 0:
        D[i] = 'Buzz'
print(*D)