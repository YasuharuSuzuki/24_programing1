A,B = map(int,input().split())
hikaku = [1,50,5,100,10,500]

if hikaku.index(A) < hikaku.index(B):
    print("B")
elif hikaku.index(A) > hikaku.index(B):
    print("A")
else:
    print("同じ")