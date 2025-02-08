N, M = map(int, input().split())

for i in range(N, M+1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz',end=' ')
    elif i % 3 == 0:
        print('Fizz',end=' ')
    elif i % 5 == 0:
        print('Buzz',end=' ')
    else:
        print(i,end=' ')

