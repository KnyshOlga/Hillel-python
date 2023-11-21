number = input("Введіть число: ")

num_lst = list(number)
print(num_lst)
while len(num_lst) > 1:
  result = 1
  for i in num_lst:
    result *= int(i)
  num_lst = list(str(result))

print(int(num_lst[0]))




