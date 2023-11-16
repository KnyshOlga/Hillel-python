first_number = int(input("Введіть перше число: "))
operator = input("Введіть оператор (+, -, *, /): ")
second_number = int(input("Введіть друге число: "))

if operator == '+':
    result = first_number + second_number
elif operator == '-':
    result = first_number - second_number
elif operator == '*':
    result = first_number * second_number
elif operator == '/':
    if second_number != 0:
        result = first_number / second_number
    else:
        result = "Помилка! Ділення на нуль неможливе."
print(result)