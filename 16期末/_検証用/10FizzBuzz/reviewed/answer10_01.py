# 入力を受け取る
N, M = map(int, input().split())

result = []
for i in range(N, M+1):
    if i % 15 == 0:
        result.append("FizzBuzz")
    elif i % 3 == 0:
        result.append("Fizz")
    elif i % 5 == 0:
        result.append("Buzz")
    else:
        result.append(str(i))

print(" ".join(result))
