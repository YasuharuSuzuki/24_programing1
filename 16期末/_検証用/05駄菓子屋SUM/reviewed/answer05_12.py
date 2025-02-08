N,S,E =map(int,input().split())
D_list = list(map(int,input().split()))
print(sum(D_list[S-1:E]))
