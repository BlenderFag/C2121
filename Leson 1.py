
class Student:
    count_of_student = 0
    def __init__(self, name, age = 15):
        self.name = name
        self.age = age
        print('Hi!')
        Student.count_of_student += 1

    def __str__(self):
        print(f'Я {self.name}, мені {self.age} років')

    def __str__(self):
        print(f'Я {self.name},і я пішов ')
        Student.count_of_student -= 1


    def grow(self):

print(Student.count_of_student)

Anton = Student('Anton')
print(Anton.age)
Kiril = Student(name = 'Kiril', age = 17)
print(Kiril.age)

print(Anton.count_of_student)
print(Student.count_of_student)

Anton.info()
Kiril.info()