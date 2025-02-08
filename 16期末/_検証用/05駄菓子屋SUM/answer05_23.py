
input_str = input()
input_list = input_str.split()
N = int(input_list[0])
S = int(input_list[1])
E = int(input_list[2])
input_str = input()
input_list = input_str.split()
D = []
for i in range(N):
  D.append(int(input_list[i]))

sum = 0
for i in range(S-1,E):
  sum += D[i]
print(sum)

