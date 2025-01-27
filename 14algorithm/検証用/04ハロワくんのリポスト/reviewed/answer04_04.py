all_word = ['Hello', 'hello', 'ハロー', 'World', 'world', 'ワールド', 'ハローワールド']
# T = input().split()
T = input()  # suzuki
H = 0

# for i in enumerate(all_word):
for i in range(len(all_word)):  # suzuki

    # if T in all_word[i] == True:
    if T.find(all_word[i]) >= 0:  # suzuki
        H += 1

if H == 2:
    print(T)
else:
    print("No")#分からない