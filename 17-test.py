# def correct_sentence(sentence):
#
#   """
#   # Виправляє речення так, щоб воно завжди починалося з великої літери та закінчувалося крапкою.
#   #
#   # Вхідні аргументи:
#   #   sentence: Речення, яке потрібно виправити.
#   #
#   # Вихідні аргументи:
#   #   Виправлене речення.
#   # """
#
#   # Отримуємо першу букву речення.
#   first_letter = sentence[0]
#
#   # Якщо перша буква не є великою літерою, замінюємо її на велику літеру.
#   if not first_letter.isupper():
#     sentence = sentence[0].upper() + sentence[1:]
#
#   # Отримуємо останню букву речення.
#   last_letter = sentence[-1]
#
#   # Якщо остання буква не є крапкою, додаємо крапку.
#   if last_letter != '.':
#     sentence = sentence + '.'
#
#   return sentence
# print(correct_sentence)

#
# def calculate_summa(a, b):
#   c = b + a
#   return c
#



# assert calculate_summa(20, 10) == 30, "Первый тест"
# assert calculate_summa(20, 40) == 60, "Второй тест"
# print('OK')
#
# def add(a, b):
#   c = a + b
#   print(c)
#
# d = add(10, 10)
# print(add(20, 10))

# Сколько значений может возвращать функция? Произвольное количество.
# def mul(a, b):
#     a *= 2
#     b *= 2
#     return a, b
#     print('Hi') #  Этот print никогда не выполнится
#
#
# a = mul(10, 20)
# print(a)

def correct_sentence(text):
  """
  Виправляє речення так, щоб воно завжди починалося з великої літери та закінчувалося крапкою.

  Вхідні аргументи:
    text: Речення, яке потрібно виправити.

  Вихідні аргументи:
    Виправлене речення.
  """

  # Отримуємо першу букву речення.
  first_letter = text[0]

  # Якщо перша буква не є великою літерою, замінюємо її на велику літеру.
  if not first_letter.isupper():
    text = first_letter.upper() + text[1:]

  # Отримуємо останню букву речення.
  last_letter = text[-1]

  # Якщо остання буква не є крапкою, додаємо крапку.
  if last_letter != '.':
    text = text + '.'

  return text


print(correct_sentence("greetings, friends") == "Greetings, friends.")
print(correct_sentence("hello") == "Hello.")
print(correct_sentence("Greetings. Friends") == "Greetings. Friends.")
print(correct_sentence("Greetings, friends.") == "Greetings, friends.")
print(correct_sentence("greetings, friends.") == "Greetings, friends.")


print(correct_sentence("greetings, friends"))
print(correct_sentence("hello"))
print(correct_sentence("Greetings. Friends"))
print(correct_sentence("Greetings, friends."))
print(correct_sentence("greetings, friends."))















