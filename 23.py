
from inspect import isgenerator


def generate_sequence(begin, end, func):

    i = 0
    while i < end:
        yield begin
        begin = func(begin)
        i += 1


def pow(x):

    return x ** 2


def test_generate_sequence():
    # Перевіряю, що створений об'єкт - це генератор
    gen_test1 = generate_sequence(2, 4, pow)
    assert isgenerator(gen_test1), 'Тест 1'

    # Перевіряю відповідність списку
    generated_list_test2 = list(generate_sequence(2, 4, pow))
    assert generated_list_test2 == [2, 4, 16, 256], 'Тест 2'


def main():
    # Приклад
    gen = generate_sequence(2, 4, pow)
    print(list(gen))


if __name__ == "__main__":
    test_generate_sequence()
    main()
