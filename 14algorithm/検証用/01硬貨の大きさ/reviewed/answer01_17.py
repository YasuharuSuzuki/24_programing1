A, B = map(int,input().split())
list1 = [1, 5, 10, 50, 100, 500]
list2 = [20.0, 22.0, 23.5, 21.0, 22.6, 26.5]

A_i = list1.index(A)
A_size = list2[A_i]

B_i = list1.index(B)
B_size = list2[B_i]

if A_size > B_size:
    print("A")
elif A_size == B_size:
    print("同じ")
else:
    print("B")