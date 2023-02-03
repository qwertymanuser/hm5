# 1 наследование
# 2 полиморфизм

# 3 инкапсуляция


class Human:
    head = 1
    brain = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def names(self):
        print(self.name, self.age)

    def __str__(self):
        return f'name is {self.name} \n' \
               f'age is {self.age}'

    def __len__(self):
        return len(self.name)

    def num(self):
        self.age = self.age * 2
        print(self.age)

    def main(self):
        print('эта функция класса человек')


class Student(Human):
    head = 2

    def __init__(self, name, age, time):
        super().__init__(name, age)
        self.time = time

    def names(self):
        super(Student, self).names()
        self.num()
        print(len(self.name))

    def main(self):
        print('эта функция класса студент')


#
student = Student('Николай', 20, 9)
hum = Human('Beka', 19)


# student.names()
# hum.names()


class Teacher(Student):
    def start(self):
        self.names()
        self.num()
        self.main()


teach = Teacher('Ислам', 18, 8)

teach.start()
