class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} টাকা জমা হলো।")
        else:
            print("ভুল পরিমাণ!")

    def withdraw(self,amount):
        if amount > self.__balance:
            print("পর্যাপ্ত ব্যালান্স নেই!")
        elif amount <= 0:
            print("ভুল পরিমাণ!")
        else:
            self.__balance -= amount
            print(f"{amount} টাকা তোলা হলো।")

    def get_balance(self):
        return self.__balance


acc = BankAccount("Pritam",5000)
acc.deposit(1000)
acc.withdraw(2000)

print(acc.get_balance())
