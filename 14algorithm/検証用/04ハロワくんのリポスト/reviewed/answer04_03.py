t = str(input())
C = t.lower()
C1 = C.replace("ハロー","hello")
C2 = C1.replace("ワールド","world")
C3 = C2.strip("!")
C4 = C3.strip("！")
C5 = C4.replace(" ","")
if C5 == "helloworld":
    print(t)
else:
    print("No")