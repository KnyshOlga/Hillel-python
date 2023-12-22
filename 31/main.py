from student import Student
from group import Group

gr = Group('PD1')

while True:
    print("1. Додати студента")
    print("2. Знайти студента")
    print("3. Видалити студента")
    print("4. Показати групу")
    print("0. Закінчити роботу")
    cmd = input("Вибрати пункт: ")

    if cmd == "1":
        first_name = input("Ім'я: ")
        last_name = input("Прізвище: ")
        age = input("Вік: ")
        gender = input("Стать: ")
        record_book = input("Номер: ")

        student = Student(first_name, last_name, age, gender, record_book)

        try:
            result = gr.add_student(student)
            print(result)
        except ValueError as e:
            print(e)
    elif cmd == "2":
        last_name = input('Введіть прізвище: ')
        found_student = gr.find_student(last_name)
        if found_student:
            print(f'Знайдений студент: {found_student}')
        else:
            print('Студент не знайдений')
    elif cmd == "3":
        last_name = input('Введіть прізвище: ')
        result = gr.delete_student(last_name)
        print(result)
    elif cmd == "4":
        print(gr)
    elif cmd == "0":
        break
    else:
        print("Ви ввели неправильне значення")