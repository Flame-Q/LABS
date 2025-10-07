class Account:
    def __init__(self, currency):
        self.currency = currency
        self.balance = 0.0

    def dep(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счёте")
        self.balance -= amount


class Client:
    def __init__(self, client_id, name):
        self.client_id = client_id
        self.name = name
        self.accounts = {}

    def open_account(self, currency):
        if currency in self.accounts:
            raise ValueError("Счёт в этой валюте уже существует")
        self.accounts[currency] = Account(currency)

    def close_account(self, currency):
        if currency not in self.accounts:
            raise ValueError("Счёт в этой валюте не существует")
        del self.accounts[currency]

    def get_account(self, currency):
        if currency not in self.accounts:
            raise ValueError("Счёт не найден")
        return self.accounts[currency]

    def total_balance(self):

    def save_statement(self):


class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = {}

    def add_client(self, client_id, name):
        if client_id in self.clients:
            raise ValueError("Клиент с таким ID уже существует")
        self.clients[client_id] = Client(client_id, name)

    def get_client(self, client_id):
        if client_id not in self.clients:
            raise ValueError("Клиент не найден")
        return self.clients[client_id]

    def transfer(self, from_acc, to_ac):

def main():
    while True:
        print("-----------БАНКОВСКАЯ СИСТЕМА------------")
        print("1. Добавить клиента")
        print("2. Войти как клиент")
        print("0. Выход")

        choice = int(input("Выбирете действие: "))

        if choice == 0:
            break

        if choice == 1:
            client_id = input("Введите ID клиента: ")
            name = input("Введите имя клиента: ")
            try: 
                Bank.add_client(client_id, name)
                print("Клиент успешно зарегистрирован")
            except ValueError as e:
                print("Ошибка:", e)

        elif choice == 2:
            client_id = input("Введите ID клиента: ")
            try:
                client = Bank.get_client(name)
            except ValueError as e:
                print("Ошибка:", e)
                continue

        while True:
            print("-----------Меню клиента------------")
            print("1. Открыть счёт")
            print("2. Закрыть счёт")
            print("3. Пополнить счёт")
            print("4. Снять деньги")
            print("5. Перевести деньги")
            print("6. Выписка по счетам деньги")
            print("0. Выйти в главное меню")

            choice2 = int(input("Выбирете действие: "))

            if choice2 == 0:
                break

            elif choice2 == 1: