n, m = map(int, input().split())
for i in range(n, m+1):
    if i % 3 == 0 and i % 5 != 0:
        print('Fizz',  end=' ')
    elif i % 3 != 0 and i % 5 == 0:
        print('Buzz',  end=' ')
    elif i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz',  end=' ')
    else:
        print(f'{i}', end=' ')

