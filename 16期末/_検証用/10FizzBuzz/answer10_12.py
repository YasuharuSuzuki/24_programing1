N,M = map(int,input().split())
count = 0
for i in range(N,M+1):
  if i % 3 == 0 and i % 5 == 0:
    print('FizzBuzz',end=' ')
    count += 1
    continue


  if i % 5 == 0:
    print('Buzz',end=' ')
    count += 1
    continue

  if i % 3 == 0:
    print('Fizz',end=' ')
    count += 1
    continue

  print(i,end=' ')
  count += 1
  if count % 10 == 0:
    print()




