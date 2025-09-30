class Client:
    def __init__(self, client_id, name):
        self.client_id = client_id
        self.name = name
        self.account = {} 

class BankAccount:
    def __init__(self, account_number, currency, client_id):
        self.account_number = account_number
        self.currency = currency
        self.client_id = client_id

def main():
    while True:
        print("-----------БАНКОВСКАЯ СИСТЕМА------------")
        print("1. Добавить клиента")
        print("2. Войти как клиент")
        print("0. Выход")

        choice1 = input("Выбирете действие: ") 

        if choice1 == "0":
            break

        if choice1 == 1:
            client_id = input("Введите ID клиента: ")
            name = input("Введите имя клиента: ")

        elif choice1 == 2:
            client_id = input("Введите ID клиента: ")

        while True:
            print("-----------Меню клиента------------")
            print("1. Открыть счёт")
            print("2. Закрыть счёт")
            print("3. Пополнить счёт")
            print("4. Снять деньги")
            print("5. Перевести деньги")
            print("6. Выписка по счетам деньги")
            print("0. Выйти в главное меню")

            choice2 = input("Выбирете действие: ") 

            if choice2 == 0:
                break

            elif choice2 == 1: