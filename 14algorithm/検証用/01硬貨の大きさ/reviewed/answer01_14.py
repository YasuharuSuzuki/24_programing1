a_c,b_c=map(int,input().split())

if a_c==1:
    a_s=1
elif a_c==50:
    a_s=2
elif a_c==5:
    a_s=3
elif a_c==100:
    a_s=4
elif a_c==10:
    a_s=5
else:
    a_s=6

if b_c==1:
    b_s=1
elif b_c==50:
    b_s=2
elif b_c==5:
    b_s=3
elif b_c==100:
    b_s=4
elif b_c==10:
    b_s=5
else:
    b_s=6

if a_s>b_s:
    print("A")
elif a_s<b_s:
    print("B")
else:
    print("同じ")