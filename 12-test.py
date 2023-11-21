# my_string_1 = 'I like Python'
# my_string_2 = "I like Python"
# my_string_3 = """#I like
# Python"""
# print(my_string_3)

# my_string_4 = 'He likes Python" # SyntaxError
# print(my_string_4)

# my_string_1 = "I 'like' Python"
# print(my_string_1)
#
# my_string_1 = 'I "like" Python'
# print(my_string_1)
#
# my_string_1 = "I \"like\" Python"
# print(my_string_1)
#
# my_string = """Python
# ""is""
# 'awesome'
# """
# print(my_string)


# x = 'Hello'World' # SyntaxError


# x = 'Hello\'World'
# print(x)

# my_string = "Hello \nworld"
# print(my_string)
#
# my_string = "Python"
# print(id(my_string))
# my_string = "JavaScript"
# print(id(my_string))

# my_string = "Python " + "is" + " awesome!"
# print(my_string)

# my_string1 = "Python"
# my_string2 = "Python1"
# my_string3 = "Python3"
# my_string4 = my_string1 + my_string2 + my_string3
# print(my_string4)

# my_string1 = "#Python"
# my_string2 = "Community"
# my_string3 = my_string1 + my_string2
# print(my_string3)

# my_string = "I " + "like" + " Python"
# print(my_string)

# my_string = "-".join(my_string)
# print(my_string)


my_string = input("Please enter string: ")

my_string = my_string.title()

acc_symb = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

new_string = "#"

for i in my_string:
    if i in acc_symb:
        new_string += i

if len(new_string) > 140:
    new_string = new_string[:140]

print(new_string)
print(len(new_string))