def common_elements():
    multiples_of_3 = [i for i in range(1, 100) if i % 3 == 0]
    multiples_of_5 = [i for i in range(1, 100) if i % 5 == 0]

    common_elements = []
    for i in multiples_of_3:
        if i in multiples_of_5:
            common_elements.append(i)

    return common_elements


common_elements = common_elements()
print(common_elements)
