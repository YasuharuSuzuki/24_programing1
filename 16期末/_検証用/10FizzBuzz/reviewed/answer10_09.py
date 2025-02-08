a, b = map(int, input().split())
for count in range(a, b+1):
    if (count%3) == 0 and (count%5) == 0
        print(f"Fizz Buzz")
    elif(count%3) == 0:
        print("Fizz")
    elif (count%5) == 0:
        print("Buzz")
    else:
        print(f"{count}")
