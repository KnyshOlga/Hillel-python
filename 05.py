lst = [4, 0, 5, 78, 3, 14]

lst1 = []
lst2 = []

len_lst = len(lst)

if len_lst % 2 == 0:
    lst1 = lst[0:int(len_lst / 2)]
    lst2 = lst[int(len_lst / 2):len_lst]

if len_lst % 2 == 1:
    lst1 = lst[0:int(len_lst / 2 + 1)]
    lst2 = lst[int(len_lst / 2 + 1):len_lst]

print(lst1)
print(lst2)
