coin_list=[1,5,10,50,100,500]
size_list=[20.0,22.0,23.5,21.0,22.6,26.5]
A,B=map(int,input().split())
indexA=coin_list.index(A);indexB=coin_list.index(B)
dataA=size_list[indexA];dataB=size_list[indexB]
if dataA>dataB:
    print("A")
elif dataA<dataB:
    print("B")
else:
    print("同じ")
