T=input()
t = T.lower()
if (t.find("hello")!=-1 or t.find("ハロー")!=-1) and (t.find("world")!=-1 or t.find("ワールド")!=-1):
    print(T)
else:
    print("No")