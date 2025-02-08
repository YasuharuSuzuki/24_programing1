N,M = map(int,input().split())
int_list = list((range(N,M+1)))

for i in range(len(int_list)):
      if int_list[i] % 3 == 0 and int_list[i] % 5 == 0:
          int_list[i] = "FizzBuzz"
      elif int_list[i] % 3 == 0:
          int_list[i] = "Fizz"
      elif int_list[i] % 5 == 0:
          int_list[i] = "Buzz"
      print(int_list[i],end=' ')
