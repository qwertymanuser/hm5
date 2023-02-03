# множественное наследование

class Учитель:
    def учить(self=1):
        print('я умею учить')


class Стороитель:
    def строить(self=1):
        print('я умею строить')


class Ученик(Учитель, Стороитель): ...


c = Ученик


# c.учить()
# c.строить()


class A:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('run A')


class B(A):
    def __init__(self, age, name):
        super().__init__(name)
        self.age = age

    def run(self):
        print('run B')


class C(B):...


a = C('name', 22)
