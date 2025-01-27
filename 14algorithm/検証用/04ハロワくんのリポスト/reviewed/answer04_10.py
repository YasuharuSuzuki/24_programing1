text = list(input())
hello_list = ['Hello','hello','ハロー']
World_list = ['World','world','ワールド']

if hello_list in text and World_list in text:
    print(text)
else:
    print('No')