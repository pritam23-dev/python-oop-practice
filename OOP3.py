# class parent():
#     def __init__(self, Name, FatherName):
#         self.__Name = Name
#         self.FatherName = FatherName
#
# p1 = parent("Pritam","Sanker")
# print(p1.FatherName ,p1.Name )
#
# print(p1.Name)
#
# # Encapsulation = concept clear....( jokhon __ use korbo na tokhon class er baire theke function , method, variable
# ei sob jekew access nite parbe i mean public hoye jabe so er solution holo ⬇️
# function , method, variable egulor age underLine(__) dite hobe , tailei ➡️ private hobe 💪


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private: বাইরে থেকে সরাসরি পাওয়া যাবে না

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} টাকা জমা হলো।")
        else:
            print("ভুল পরিমাণ!")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("পর্যাপ্ত ব্যালেন্স নেই!")
        elif amount <= 0:
            print("ভুল পরিমাণ!")
        else:
            self.__balance -= amount
            print(f"{amount} টাকা তোলা হলো।")

    def get_balance(self):
        return self.__balance


acc = BankAccount("Pritam", 5000)
acc.deposit(1000)
acc.withdraw(2000)
print(acc.get_balance())   # 4000

# সরাসরি বদলানোর চেষ্টা
acc.__balance = 1000000 # এটা আসল balance বদলাবে না
print(acc.get_balance())   # এখনো 4000

# acc.owner = "karim"
# print(acc.owner)   # owner __ kori nai tai etir access newa galo 👀