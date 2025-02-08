N,M = map(int, input().split())
s = ""

for i in range(N, M+1):
    if ((i % 3) == 0) and ((i % 5) == 0):
        s += "FizzBuzz"
    elif ((i % 3) == 0):
        s += "Fizz"
    elif ((i % 5) == 0):
        s += "Buzz"
    else:
        s += str(i)
    s += " "
print(s)