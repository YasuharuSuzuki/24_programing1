ko,f,l=map(int,input().split())
dagasi=list(map(int,input().split()))

nedan=0
for count in range(f-1,l):
    nedan=nedan+dagasi[count]

print(nedan)
