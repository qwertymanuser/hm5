import random


class SlotMachine:
    def init(self, name):
        self.name = name
        self.__user_balance = 100
        self.__game_balance = 0

    def info(self):
        return f"Name: {self.name}, User-Balance: {self.__user_balance}, Game-Balance: {self.__game_balance}"

    def top_up_balance(self, balance):
        if balance <= 100:
            self.__balace_up(balance)
            return f"{self.name} вы пополнили свой баланс {self.__game_balance}"
        else:
            return f"вы можете пополнить баланс до 100$"

    def __balace_up(self, balance):
        self.__user_balance -= balance
        self.__game_balance += balance

    def game(self):
        randomi = random.randint(1, 10)
        popytky = 0
        while True:
            user = int(input("Ведите число от 1 до 10: "))
            popytky += 1
            if randomi == user:
                self.__game_balance += 50
                return f"Вы выиграли ваш баланс: {self.__game_balance}"

            else:
                if 5 - popytky == 0:
                    self.__game_balance -= 10

                    return f"Вы проиграли ваш баланс {self.__game_balance}"

    def conslusion_money(self, money):
        if money > 50:
            self.__conslusion_money(money)
            return f"{self.name} вы пополнили свой баланс {self.__user_balance}"
        else:
            return "Вывести можно от 50$"

    def __conslusion_money(self, money):
        self.__game_balance -= money
        self.__user_balance += money


    def main(self):
        while True:
            try:
                comanda = int(input(
                    "1 - информация, 2 - пополнение игрового баланса, 3 - игра, 4 - перевод денег на основной счёт: "))
                if comanda == 1:
                    print(f"{self.info()}")
                elif comanda == 2:
                    user = int(input("Cколько вы хотить перевести: "))
                    if user >= 50:
                        print(f"{self.top_up_balance(user)}")
                    else:
                        print("пополнить можно не меньше 50$")
                        print(f"{comanda}")
                elif comanda == 3:
                    print(f"{self.game()}")
                elif comanda == 4:
                    user = int(input("Cколько вы хотить перевести: "))
                    if user >= 50:
                        print(f"{self.conslusion_money(user)}")
                    else:
                        print("обноличить можно не меньше 50$")
                else:
                    print(comanda)
            except:
                print("Шлюха блять")


slot = SlotMachine("askhat")
print(slot.main())
