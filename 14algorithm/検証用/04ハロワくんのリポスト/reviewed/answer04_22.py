import re

def solve():
    text = input()

    hello_pattern = r"(Hello|hello|ハロー)"
    world_pattern = r"(World|world|ワールド)"

    pattern = r"^" + hello_pattern + r"\s?" + r"(World|world|ワールド|World!|world!|ワールド！|World！)" + r"$"

    if re.match(pattern, text):
        print(text)
    else:
        print("No")

solve()
