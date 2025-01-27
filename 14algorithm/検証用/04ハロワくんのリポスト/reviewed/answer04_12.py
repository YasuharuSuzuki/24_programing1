T = input()

if T in ["Hello", "hello", "ハロー"]:
    T_hello = T
    if T in ["World", "world", "ワールド"]:
        T_world = T

        print(T_hello + T_world)
else:
    print("No")