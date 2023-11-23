# def common_elements():
#     multiples_of_3 = [i for i in range(1, 100) if i % 3 == 0]
#     multiples_of_5 = [i for i in range(1, 100) if i % 5 == 0]
#
#     common_elements = []
#     for i in multiples_of_3:
#         if i in multiples_of_5:
#             common_elements.append(i)
#
#     return common_elements
#
# common_elements = common_elements()
# print(common_elements)


# 3. Базові операції над множинами. Перелік
# Мова Python підтримує наступні операції над множинами:
#
# in – перевірка елементу на входження в множину;
# – (мінус) – різниця множин;
# | – об’єднання множин;
# & – перетин множин;
# ^ – симетрична різниця.


def common_elements():
    multiples_of_3 = [i for i in range(1, 100) if i % 3 == 0]
    multiples_of_5 = [i for i in range(1, 100) if i % 5 == 0]

    print(multiples_of_3)
    print(multiples_of_5)

    multiples_of_3_set = set(multiples_of_3)
    multiples_of_5_set = set(multiples_of_5)

    common_elements_set = multiples_of_3_set & multiples_of_5_set

    return common_elements_set


common_elements = common_elements()
print(common_elements)

#Вибачте не можу втриматися, щоб не перевірити код наглядно
