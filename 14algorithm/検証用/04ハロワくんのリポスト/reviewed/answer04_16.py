T = input()
A =  T.lower()
A1 = A.replace("ハロー","hello")
A2 = A1.replace("ワールド","world")
A3 = A2.strip("!")
A4 = A3.strip("！")
A5 = A4.replace(" ","")
if A5 == "helloworld":
    print(T)
else:
    print("No")


