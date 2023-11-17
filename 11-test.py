def calculator(first_number, second_number, operator):

  if operator == "+":
    return first_number + second_number
  elif operator == "-":
    return first_number - second_number
  elif operator == "*":
    return first_number * second_number
  elif operator == "/":
    if second_number != 0:
      return first_number / second_number
    else:
      return "Помилка! Ділення на нуль неможливе."


def main():
  """Основна функція."""

  # Виконуємо код

  while True:
    first_number = int(input("Введіть перше число: "))
    second_number = int(input("Введіть друге число: "))
    operator = input("Введіть оператор (+, -, *, /): ")

    result = calculator(first_number, second_number, operator)
    print(result)

    reset = input("Бажаєте продовжити? (так/ні): ")
    if reset.lower() not in ["так", "ні"]:
      print("Помилка! Будь ласка, введіть 'так' або 'ні'.")
      continue

    if reset.lower() == "ні":
      break


if __name__ == "__main__":
  main()
