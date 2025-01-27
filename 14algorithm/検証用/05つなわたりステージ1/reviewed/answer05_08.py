T = input()
list1 =list(T)
i = 0
k = 0
for count in range(len(T)):
    if list1[i] == 'R':
        k = k-1
        i = i+1
    elif list1[i] == 'L':
        k = k+1
        i = i+1
    elif list1[i] == 'N':
        i = i+1
if k>=4 or k<=-4:
    print('YOU LOST')
else:
    print('GOAL')

