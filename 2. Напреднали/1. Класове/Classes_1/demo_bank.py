import datetime
import uuid


class Account:
    def __init__(self, initial_amount, customer_id):
        self.balance = initial_amount
        self.id = uuid.uuid1()
        self.owner = customer_id

    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    def withdraw(self, withdraw_amount):
        if self.balance <= withdraw_amount:
            self.balance -= withdraw_amount
        else:
            print('Insufficient balance')

    def is_negative(self):
        if self.balance < 0:
            return True
        else:
            return False


class Customer:
    def __init__(self, first_name, last_name, address, customer_id, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.id = customer_id
        # self.age = self.date_of_birth = datetime.strptime(date_of_birth, '%d-%m-%Y')

    def get_age(self):
        """ Calculates and returns the customer's age. """
        today = datetime.today()
        try:
            birthday = self.date_of_birth.replace(year=today.year)
        except ValueError:
            # birthday is 29 Feb but today's year is not a leap year
            birthday = self.date_of_birth.replace(year=today.year,
                                               day=self.date_of_birth.day - 1)
        if birthday > today:
            return today.year - self.date_of_birth.year - 1
        return today.year - self.date_of_birth.year


customer1 = Customer('Ivan', 'Petrov', 'Sofia 1000', 23432343, "12-05-01")

account1 = Account(59, 23432343)
account2 = Account(40000050, 23432343)

print(account1.balance)
account1.deposit(100)
print(account1.balance)
print(account1.id)
