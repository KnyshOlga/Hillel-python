#Один варіант
lst = [4, 0, 5, 0, 0, 14, 22]
lst1 = []
lst2 = []
for i in lst:
    if i == 0:
        lst2.append(i)
    else:
        lst1.append(i)
lst_result = lst1 + lst2
print(lst_result)


#Другий варіант
lst = [4, 0, 5, 0, 0, 14, 22, -1]
for i in lst:
    if i == 0:
        lst.remove(i)
        lst.append(i)
print(lst)

