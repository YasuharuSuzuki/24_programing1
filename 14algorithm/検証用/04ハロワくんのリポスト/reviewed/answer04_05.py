T = input()
t_lower = T.lower()
if ("hello" in t_lower) or ("ハロー" in t_lower) and  ("world" in t_lower) or ("ワールド" in t_lower):
    print(T)
else:
    print("No")