from typing import TextIO
T = input()

if (("Hello" in T) or ("hello" in T) or ("ハロー" in T) == True) and (("World" in T) or ("world" in T) or ("ワールド" in T) == True):
    print(T)

else:
    print("No")
