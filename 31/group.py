from student import Student


class Group:
    def __init__(self, number, max_students=2):
        self.number = number
        self.group = []
        self.max_students = max_students

    def add_student(self, student):
        if len(self.group) < self.max_students:
            self.group.append(student)
            return 'Студент доданий'
        else:
            raise ValueError('В групі вже максимальна кількість студентів')

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)
            return 'Студент видалений'
        else:
            return 'Студент не знайдений'

    def find_student(self, last_name):
        last_name = input('Введіть прізвище: ')
        for student in self.group:
            if last_name in str(student):
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(map(str, self.group))
        return f'Group: {self.number}\n{all_students}'

