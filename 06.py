list = [12, 3, 4, 10, -2, 8]

if len(list) == 0:
    print(list)
elif len(list) < 1:
    print(list)
else:
    list.insert(0, list[-1])
    list.pop(-1)
    print(list)

