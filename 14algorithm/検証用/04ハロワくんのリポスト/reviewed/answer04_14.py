t = input()

patterns = [
    "Hello World!",
    "Hello World",
    "hello world!",
    "hello world",
    "ハローワールド！",
    "ハローワールド",
    "ハローWorld！",
    "ハローWorld"
]

if t in patterns:
    print(t)
else:
    print("No")

