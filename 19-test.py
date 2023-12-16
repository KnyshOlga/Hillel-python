# import string
#
#
# def is_palindrome(text):
#     punctuation = string.punctuation
#     text = text.lower().translate(str.maketrans('', '', punctuation))
#
#     reversed_text = text[::-1]
#
#     text = text.strip()
#     reversed_text = reversed_text.strip()
#
#     return text == reversed_text
#
#
# assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
# assert is_palindrome('aurora') == False, 'Test4'
# print("ОК")

def is_palindrome(text):
    # Видаляємо всі знаки пунктуації та переводимо рядок у нижній регістр
    cleaned_text = ''.join(char.lower()

     for char in text
     if char.isalnum())

    # Перевертаємо рядок і порівнюємо його з оригіналом
    return cleaned_text == cleaned_text[::-1]


# Тести
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
