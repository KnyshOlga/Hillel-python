import string
letters = string.ascii_letters
my_string = input("Please enter letters : ")
start = letters.index(my_string[0])
end = letters.index(my_string[2]) + 1
print(letters[start:end])