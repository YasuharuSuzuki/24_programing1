def solve():
    t = input()

    hello_patterns = ["Hello", "hello", "ハロー"]
    hello_match = False
    for pattern in hello_patterns:
        if t.startswith(pattern):
            hello_match = True
            break

    world_patterns = ["World", "world", "ワールド"]
    world_match = False
    if hello_match:
        remaining_str = t[len(hello_patterns[0]):]

        if remaining_str.startswith(" "):
          remaining_str = remaining_str[1:]

          for pattern in world_patterns:
            if remaining_str.startswith(pattern):
                world_match = True
                break

    if hello_match and world_match:
        print(t)
    else:
        print("No")

solve()