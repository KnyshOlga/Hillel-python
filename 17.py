
def correct_sentence(text):

  first_letter = text[0]

  if not first_letter.isupper():
    text = first_letter.upper() + text[1:]

  last_letter = text[-1]

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
