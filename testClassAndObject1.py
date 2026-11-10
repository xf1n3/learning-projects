class BankAccount:
    def __init__(self, name, balance, deposit_method, withdrawal_method):
        self.name = name
        self.balance = balance
        self.deposit_method = deposit_method
        self.withdrawal_method = withdrawal_method
        self.history = []
        
    def show_balance(self):
        return self.balance
    
    def withdraw_function(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.history.append(f"Снято: {amount}")
        else:
            print("Вы не можете снять сумму больше той которая у вас на балансе")

    def deposit_function(self, amount):
        if amount <= 0:
            print("Нельзя положить сумму равную или меньше 0")
        else:
            self.balance += amount
            self.history.append(f"Добавлено: {amount}")

    def transfer_function(self, anotherbank, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            anotherbank.balance += amount
            self.history.append(f"Переведено: {amount} для {anotherbank.name}")
            anotherbank.history.append(f"Получено: {amount} от {self.name}")
        else:
            print("Сумма меньше нуля, либо банк не найден")
    def show_history(self):
        return self.history


bankaccount1 = BankAccount("alex", 10000, "online", "bankomat")
bankaccount2 = BankAccount("david", 15000, "personally", "without card")

bankaccount1.transfer_function(bankaccount2, 5000)

print(bankaccount1.show_history(), bankaccount2.show_history())
