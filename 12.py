my_string = input("Please enter string: ")
my_string = my_string.title()

accept_symb = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

new_string = "#"

for i in my_string:
    if i in accept_symb:
        new_string += i

if len(new_string) > 140:
    new_string = new_string[:140]

print(new_string)
print(len(new_string))