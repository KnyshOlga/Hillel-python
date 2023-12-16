class Human:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'Human {self.first_name} {self.last_name}, {self.gender} {self.age} y.o.'


class Student(Human):
    def __str__(self):
        return f'Student {self.first_name} {self.last_name}, {self.gender} {self.age} y.o.'


class Group:
    def __len__(self):
        return len(self.students)

    def __init__(self):
        self.students = []

    def __str__(self):
        return 'Group:\n' + '\n'.join(f'{n + 1}. {s}' for n, s in enumerate(self.students))

    def add_student(self, student):
        self.students.append(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.students.remove(student)

    def find_student(self, last_name):
        for s in self.students:
            if s.last_name == last_name:
                return s
        return None


sarah = Human('Sarah', 'Connor', 40, 'female')
assert str(sarah) == 'Human Sarah Connor, female 40 y.o.', \
    'Human object representation is invalid'

john = Student('John', 'Connor', 20, 'male')
assert str(john) == 'Student John Connor, male 20 y.o.', \
    'Student object representation is invalid'

group = Group()
assert len(group) == 0, 'Group is not empty'

group.add_student(Student('Cristiano', 'Ronaldo', 38, 'male'))
group.add_student(Student('Emma', 'Watson', 33, 'female'))
group.add_student(Student('Johnny', 'Depp', 60, 'male'))
assert len(group) == 3, 'Count of students is wrong'
assert str(group) == '''Group:
1. Student Cristiano Ronaldo, male 38 y.o.
2. Student Emma Watson, female 33 y.o.
3. Student Johnny Depp, male 60 y.o.''', \
    'Group object representation is invalid'

student1 = group.find_student('Watson')
assert str(student1) == 'Student Emma Watson, female 33 y.o.'

student2 = group.find_student('Madonna')
assert student2 is None, 'This student is not in the group'

group.delete_student('Ronaldo')
assert len(group) == 2, 'Count of students is wrong'
assert str(group) == '''Group:
1. Student Emma Watson, female 33 y.o.
2. Student Johnny Depp, male 60 y.o.''', \
    'Group object representation is invalid'

group.delete_student('Depp')
assert len(group) == 1, 'Count of students is wrong'
assert str(group) == '''Group:
1. Student Emma Watson, female 33 y.o.''', \
    'Group object representation is invalid'

group.delete_student('Watson')
assert len(group) == 0, 'Count of students is wrong'
assert str(group) == '''Group:
''', 'Group object representation is invalid'

