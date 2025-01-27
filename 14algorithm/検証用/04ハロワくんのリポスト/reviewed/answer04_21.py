import re

def solve():
    text = input()
    hello_pattern = r"^(Hello|hello|ハロー)"
    world_pattern = r"(World|world|ワールド)[!！]?$"

    hello_match = re.match(hello_pattern, text)
    world_match = re.search(world_pattern, text)

    if hello_match and world_match:
        print(text)
    else:
        print("No")
solve()