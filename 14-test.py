#Перший спосіб

number = input("Введіть число: ")  #получаем строку

num_lst = list(number)             #из строки делаем список ( список с елементами)
print(num_lst)
while len(num_lst) > 1:            #Пров. что в списке не более одного елемента
  result = 1                       #Заводим переменную которую будем перемножать елементі списка
  for i in num_lst:                #бежим по списку и кажд елемент помещаем в і
    result *= int(i)               #Приводим і  к числу и умножаем
  num_lst = list(str(result))      #Список приводим к строке с результатом

print(int(num_lst[0]))


#Другий спосіб
number = input("Введіть число: ")  #получаем строку

while len(number) > 1:
  result = 1
  for i in number:
    result *= int(i)
  number = str(result)

print(int(number))




