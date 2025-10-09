class Client:
    def __init__(self, client_id, name):
        self.client_id = client_id
        self.name = name
        self.accounts = {}

class BankAccount:
    def __init__(self, account_number, currency, client_id):
        self.account_number = account_number
        self.currency = currency
        self.balance = 0.0
        self.client_id = client_id
        self.is_active = True
        self.history = []

    def add_operation(self, operation_type, amount, description=""):
        operation = {
            "type": operation_type,
            "amount": amount,
            "balance_after": self.balance,
            "description": description
        }
        self.history.append(operation)

class Bank:
    def __init__(self):
        self.clients = {}
        self.accounts = {}
        self.next_acc_num = 1
        self.available_currencies = ["BYN", "RUB", "USD", "EUR"]
    
    def create_client(self, client_id, name):
        if client_id in self.clients:
            raise Exception("Клиент с таким ID уже существует")
        self.clients[client_id] = Client(client_id, name)
    
    def show_currencies_menu(self):
        print("\nДоступные валюты:")
        i = 1
        for currency in self.available_currencies:
            print(str(i) + ". " + currency)
            i += 1
    
    def open_account(self, client_id, currency):
        if client_id not in self.clients:
            raise Exception("Клиент не найден")
        
        client = self.clients[client_id]
        
        if currency in client.accounts:
            raise Exception("У клиента уже есть счет в этой валюте")
        
        account_number = "ACC" + str(self.next_acc_num)
        self.next_acc_num += 1
        
        account = BankAccount(account_number, currency, client_id)
        self.accounts[account_number] = account
        client.accounts[currency] = account
        
        account.add_operation("OPEN_ACCOUNT", 0, "Открытие счета")
        
        return account_number
    
    def close_account(self, client_id, account_number):
        if client_id not in self.clients:
            raise Exception("Клиент не найден")
        
        if account_number not in self.accounts:
            raise Exception("Счет не найден")
        
        account = self.accounts[account_number]
        
        if account.client_id != client_id:
            raise Exception("Этот счет не принадлежит данному клиенту")
        
        if account.balance > 0:
            raise Exception("Нельзя закрыть счет с положительным балансом")
        
        account.is_active = False
        account.add_operation("CLOSE_ACCOUNT", 0, "Закрытие счета")
        client = self.clients[client_id]
        del client.accounts[account.currency]
        del self.accounts[account_number]
    
    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            raise Exception("Счет не найден")
        
        account = self.accounts[account_number]
        
        if not account.is_active:
            raise Exception("Счет закрыт")
        
        if amount <= 0:
            raise Exception("Сумма должна быть положительной")
        
        account.balance += amount
        account.add_operation("DEPOSIT", amount, "Пополнение счета")
    
    def withdraw(self, client_id, account_number, amount):
        if account_number not in self.accounts:
            raise Exception("Счет не найден")
        
        account = self.accounts[account_number]
        
        if account.client_id != client_id:
            raise Exception("Этот счет не принадлежит данному клиенту")
        
        if not account.is_active:
            raise Exception("Счет закрыт")
        
        if amount <= 0:
            raise Exception("Сумма должна быть положительной")
        
        if amount > account.balance:
            raise Exception("Недостаточно средств на счете")
        
        account.balance -= amount
        account.add_operation("WITHDRAW", amount, "Снятие со счета")
    
    def transfer(self, from_client_id, from_account_number, to_account_number, amount):
        if from_account_number not in self.accounts:
            raise Exception("Счет отправителя не найден")
        
        if to_account_number not in self.accounts:
            raise Exception("Счет получателя не найден")
        
        from_account = self.accounts[from_account_number]
        to_account = self.accounts[to_account_number]
        
        if from_account.client_id != from_client_id:
            raise Exception("Этот счет не принадлежит данному клиенту")
        
        if not from_account.is_active or not to_account.is_active:
            raise Exception("Один из счетов закрыт")
        
        if from_account.currency != to_account.currency:
            raise Exception("Валюты счетов не совпадают")
        
        if amount <= 0:
            raise Exception("Сумма должна быть положительной")
        
        if amount > from_account.balance:
            raise Exception("Недостаточно средств на счете отправителя")
        
        from_account.balance -= amount
        to_account.balance += amount
        
        from_account.add_operation("TRANSFER_OUT", amount, "Перевод на счет " + to_account_number)
        to_account.add_operation("TRANSFER_IN", amount, "Перевод от счета " + from_account_number)
    
    def get_client_accounts(self, client_id):
        if client_id not in self.clients:
            raise Exception("Клиент не найден")
        
        return self.clients[client_id].accounts
    
    def save_statement(self, client_id, filename):
        if client_id not in self.clients:
            raise Exception("Клиент не найден")
        
        client = self.clients[client_id]
        
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("Выписка по счетам клиента: " + client.name + " (ID: " + client_id + ")\n")
            file.write("=" * 50 + "\n")
            
            total_balance = 0
            
            for currency, account in client.accounts.items():
                if account.is_active:
                    file.write("Счет: " + account.account_number + "\n")
                    file.write("Валюта: " + currency + "\n")
                    file.write("Баланс: " + str(round(account.balance, 2)) + "\n")
                    file.write("История операций:\n")
                    
                    if account.history:
                        for operation in account.history:
                            operation_type = operation["type"]
                            amount = operation["amount"]
                            balance = operation["balance_after"]
                            description = operation["description"]
                            
                            if operation_type == "OPEN_ACCOUNT":
                                file.write("  - Открытие счета\n")
                            elif operation_type == "CLOSE_ACCOUNT":
                                file.write("  - Закрытие счета\n")
                            elif operation_type == "DEPOSIT":
                                file.write("  - Пополнение: +" + str(amount) + " (Баланс: " + str(round(balance, 2)) + ")\n")
                            elif operation_type == "WITHDRAW":
                                file.write("  - Снятие: -" + str(amount) + " (Баланс: " + str(round(balance, 2)) + ")\n")
                            elif operation_type == "TRANSFER_OUT":
                                file.write("  - Перевод: -" + str(amount) + " (Баланс: " + str(round(balance, 2)) + ") - " + description + "\n")
                            elif operation_type == "TRANSFER_IN":
                                file.write("  - Перевод: +" + str(amount) + " (Баланс: " + str(round(balance, 2)) + ") - " + description + "\n")
                    else:
                        file.write("  - Операций нет\n")
                    
                    file.write("-" * 30 + "\n")
                    total_balance += account.balance
            
            file.write("Общий баланс: " + str(round(total_balance, 2)) + "\n")

def main():
    bank = Bank()
    
    while True:
        print("\n=== БАНКОВСКАЯ СИСТЕМА ===")
        print("1. Войти в систему")
        print("2. Создать нового клиента")
        print("0. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            client_id = input("Введите ваш ID клиента: ")
            
            if client_id not in bank.clients:
                print("Клиент с таким ID не найден")
                continue
            
            client = bank.clients[client_id]
            print("\nДобро пожаловать, " + client.name + "!")
            
            while True:
                print("\n=== ДОСТУПНЫЕ ОПЕРАЦИИ ===")
                print("1. Показать мои счета")
                print("2. Открыть новый счет")
                print("3. Закрыть счет")
                print("4. Пополнить счет")
                print("5. Снять деньги")
                print("6. Перевести деньги")
                print("7. Сохранить выписку в файл")
                print("0. Выйти из системы")
                
                operation = input("Выберите операцию: ")
                
                try:
                    if operation == "1":
                        accounts = bank.get_client_accounts(client_id)
                        if not accounts:
                            print("У вас нет открытых счетов")
                        else:
                            print("\nВаши счета:")
                            for currency, account in accounts.items():
                                status = "активен" if account.is_active else "закрыт"
                                print("Счет " + account.account_number + ": " + currency + " - " + str(round(account.balance, 2)) + " (" + status + ")")
                    
                    elif operation == "2":
                        bank.show_currencies_menu()
                        currency_choice = input("Выберите валюту (1-4): ")
                        
                        if currency_choice == "1":
                            currency = "BYN"
                        elif currency_choice == "2":
                            currency = "RUB"
                        elif currency_choice == "3":
                            currency = "USD"
                        elif currency_choice == "4":
                            currency = "EUR"
                        else:
                            print("Неверный выбор валюты")
                            continue
                            
                        account_number = bank.open_account(client_id, currency)
                        print("Счет " + account_number + " в валюте " + currency + " успешно открыт")
                    
                    elif operation == "3":
                        account_number = input("Введите номер счета для закрытия: ")
                        bank.close_account(client_id, account_number)
                        print("Счет успешно закрыт")
                    
                    elif operation == "4":
                        account_number = input("Введите номер счета: ")
                        amount = float(input("Введите сумму для пополнения: "))
                        bank.deposit(account_number, amount)
                        print("Счет успешно пополнен")
                    
                    elif operation == "5":
                        account_number = input("Введите номер счета: ")
                        amount = float(input("Введите сумму для снятия: "))
                        bank.withdraw(client_id, account_number, amount)
                        print("Снятие успешно выполнено")
                    
                    elif operation == "6":
                        from_account = input("Введите номер вашего счета: ")
                        to_account = input("Введите номер счета получателя: ")
                        amount = float(input("Введите сумму для перевода: "))
                        bank.transfer(client_id, from_account, to_account, amount)
                        print("Перевод успешно выполнен")
                    
                    elif operation == "7":
                        filename = "check.txt"
                        bank.save_statement(client_id, filename)
                        print("Выписка сохранена в файл " + filename)
                    
                    elif operation == "0":
                        print("Выход из системы...")
                        break
                    
                    else:
                        print("Неверный выбор операции")
                
                except Exception as e:
                    print("Ошибка: " + str(e))
        
        elif choice == "2":
            try:
                client_id = input("Введите ID нового клиента: ")
                name = input("Введите имя нового клиента: ")
                bank.create_client(client_id, name)
                print("Клиент " + name + " успешно создан!")
            except Exception as e:
                print("Ошибка при создании клиента: " + str(e))
        
        elif choice == "0":
            print("До свидания!")
            break
        
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()