a = int(input("Please enter number:"))

b = 0

while a > 0:
   z = a % 10
   a //= 10
   b *= 10
   b += z

print(b)