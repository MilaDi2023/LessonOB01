# Задание для отработки навыков  работы с классами и объектами
#
# Задача: простая учетная система банка
# Определите класс Account, имитирующий банковский счёт
# Класс должен включать атрибуты для хранения идентификатора владельца,
# баланса счёта и методы для депозита(пополнения) и снятия средств, если
# на счету достаточно денег.

class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def info(self): # Метод - выдача информации о владельце счета и его балансе
        print(f"Владелец счёта - {self.id}")
        print(f"Текущий баланс счёта - {self.balance} руб.")

    def deposit(self, money): # Метод - пополнение счёта
        if money > 0:
            self.balance = self.balance + money
            print(f"Вы успешно пополнили счёт на {money} руб. Ваш баланс - {self.balance} руб.")

    def withdraw(self, money): # Метод - снятие со счёта
        if money > self.balance:
            print(f"На вашем счёте недостаточно средств")
        elif money <= self.balance:
            self.balance = self.balance - money
            print(f"Вы успешно сняли со счёта {money} руб. Ваш баланс - {self.balance} руб.")

man = Account("Вася Пупкин", 1700)

man.info()
man.deposit(300)
man.withdraw(400)