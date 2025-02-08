N, M = map(int,input().split())
A = list()
for count in range(N, M+1):
    if (count % 3) == 0 and (count % 5) == 0:
        A.append("FizzBuzz")
    elif (count % 3) == 0:
        A.append("Fizz")
    elif (count % 5) == 0:
        A.append("Buzz")
    else:
        A.append(count)

for i in A:
    print(i, end=" ")
