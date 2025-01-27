T = input()
T.lower()
for i in range(len(T)):
    T.replace('ハロー','hello')
    T.replace('ワールド','world')
    T.replace('ハローワールド','helloworld')

if T.find('helloworld'):
    print(T)
else:
    print('No')