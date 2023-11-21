import keyword
import string

my_string = input("Введіть будь-ласка речення: ")

deny_symbol = string.punctuation
deny_symbol = deny_symbol.replace("_", "") + " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lst = keyword.kwlist

result = True

if my_string[0] in "0123456789":
    result = False
elif my_string in lst:
    result = False
else:
    for i in my_string:
        if i in deny_symbol:
            result = False

print(result)


