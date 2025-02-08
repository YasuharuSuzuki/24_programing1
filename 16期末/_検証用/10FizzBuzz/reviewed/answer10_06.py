N, M = map(int, input().split())

baisuu = [""]

for i in range(N, M+1):
    if i % 3 ==0 and i % 5 ==0:
        baisuu.append( "FizzBuzz ")

    elif i % 3 == 0:
        baisuu.append("Fizz ")

    elif i % 5 == 0:
        baisuu.append("Buzz " )

    else:
        baisuu.append(f"{i} ")

for a in baisuu:
    print(a, end = "")

