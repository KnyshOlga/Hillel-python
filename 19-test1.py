# Введення рядка для перевірки на паліндром
user_input = input("Введіть рядок для перевірки на паліндром: ")

# Видалення знаків пунктуації та переведення в нижній регістр
cleaned_text = ''.join(char.lower() for char in user_input if char.isalnum())

# Використання двох покажчиків для порівняння символів
left, right = 0, len(cleaned_text) - 1
is_palindrome = True

while left < right:
    if cleaned_text[left] != cleaned_text[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

# Виведення результату
if is_palindrome:
    print("Введений рядок - паліндром.")
else:
    print("Введений рядок - не паліндром.")
