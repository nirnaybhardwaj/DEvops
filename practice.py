
class Account:
    def __init__(self, bal, acc):
        self.bal = bal
        self.acc = acc

    def debit(self, amount):
        self.bal -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.print_bal())

    def credit(self, amount):
        self.bal += amount
        print("Rs.", amount, "was credited")
        print("total balance = ", self.print_bal())

    def print_bal(self):
        return self.bal

acc1 = Account(10000, 12345)
acc2 = Account(20000, 98765)
print(acc1.bal)
print(acc1.acc)

acc1.debit(3000)

acc1.credit(2000)







