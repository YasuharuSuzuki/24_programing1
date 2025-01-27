post=str(input())

if (("Hello" in post) or ("hello" in post) or ("ハロー"in post)) and (("World" in post) or ("world" in post) or ("ワールド"in post)):
    print(post)
else:
    print("No")