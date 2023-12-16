def is_even(number):
    while number % 2 == 0:
        number //= 2
    return number == 1


    assert is_even(2494563894038 ** 2) == True, 'Test1'
    assert is_even(1056897 ** 2) == False, 'Test2'
    assert is_even(24945638940387 ** 3) == False, 'Test3'
