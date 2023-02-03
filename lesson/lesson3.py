# инкапсуляцию
# публичный без нижних подчеркиваний
# защищенный с одним нижним подчеркиванием
# 3 скрытый с 2 нижними подчеркиваниями


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def may(self):
        print(f'{self.name} may\n'
              f'age is {self.age}')


cat = Cat('бека', 4)


# cat.may()


class Person:
    def __init__(self, name, last_name, age, key):
        self._name = name
        self._last = last_name
        self.__age = age
        self.__key = key


    def set_age(self, age):
        if age > 1 or age < 130:
            self.__age = age
        else:
            raise ValueError(f'возраст не может быть меньше 0 и больше 130')

    def get_age(self):
        print(self.__age)
    def keys(self):
        print(self._name)

    def _s(self):
        print(self.__key)


# per2 = Person('name', 'aa', 11, 'tcfyvgubhjb')

per1 = Person('beka', 'D.Y', 19, '1234567')
per1.set_age(12)
per1.get_age()
# per1._name = 'ivan'
# per1._Person__key = 1

# per1.keys()
#
# per1._s()

p = 'eyrfhdhs'


# print(dir(per1))


# print(dir(p))
# print(p.upper())


class Micro:
    def __init__(self, name):
        self.name = name

    def on(self):
        self.time()
        print('start')

    def time(self):
        print('input time')

    def _off(self):
        self.stop()

    def open(self):
        print('при открытии двери микроволновка автоматически остонавливается ')
        self._off()

    def stop(self):
        print('stop')

c = Micro('samsung')


# c.on()
# c.open()
# c._off()


class Чайник:
    def __init__(self, name):
        self.name = name

    def on(self):
        self._on()
        self._woter()

    def _on(self):
        print('включить чайник')

    def _woter(self):
        print('нагревать воду')

    def off(self):
        print('выключить')


h = Чайник('tefal')
# h.on()
# h._woter()
print('это lesson 3')