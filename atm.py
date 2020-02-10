import random

class BaseATM():
    """
      The constructor class for all atms. Sets up balance variable to 0.0.
    """
    def __init__(self, balance=0.0):
        self.balance = balance

    def withdraw(self, quantity):
        """
          Withdraws a certain quantity from the account unless the account would go negative.

          Args:
            quantity: quantity of cash to remove
        """
        # If there isn't enough money left stop the transaction
        if self.balance - quantity < 0:
            print('There is not enough currency to withdraw that amount')
            return self.check_balance()
        # Remove the money from the account and return the new balance
        self.balance -= quantity
        return self.check_balance()

    def deposit(self, quantity):
        """
          Deposits a certain amount into the account.

          Args:
            quantity: quantity of cash to remove
        """
        # Deposit currency and return new balance
        self.balance += quantity
        return self.check_balance()

    def check_balance(self):
        """
          Displays the balance for the user and returns it.
        """
        print(self.balance)
        return self.balance
        
class CoachATM(BaseATM):
    """
      An atm that inherits from BaseATM, but helps users whenever they deposit money
    """
    def deposit(self, quantity):
        """
          Functions identical to the normal deposit, but occasionally gives an extra dollar.
          Also displays an encouraging message.
        """
        print('Great Work!')
        if random.randrange(0, 20) == 7:
            print('Here is an extra dollar. Keep it up!')
            super.balance += 1
        return super().deposit(quantity)

class LoanSharkATM(BaseATM):
    """
      An atm that inherist from BaseATM, but allows the user to overdraw and encurs fees when they do.
    """
    def __init__(self, balance=0.0):
        super().__init__(balance=balance)
        # Initial fee for overdrawing, double every time
        self.fee = 15.00

    def withdraw(self, quantity):
        """
          Withdraws a certain quantity from the account no matter what. Incurs fees that increase each time
          the account goes negative and resets when it returns positive
        """
        super.balance -= quantity
        # Incur penalty if negative
        if super.balance < 0:
            super.balance -= self.fee
            self.fee *= 2
        return super.check_balance()
    
    def deposit(self, quantity):
        balance = super().deposit(quantity)
        if super.balance < 0:
            # Reset fee
            self.fee = 15.00
        return balance

class SnarkyATM(BaseATM):
    """
      An atm that inherist from BaseATM, but mocks the user every time they deposit or withdraw.
    """
    def deposit(self, quantity):
        print(f'Only depositing {quantity}, that\'s nothing!')
        return super().deposit(quantity)

    def withdraw(self, quantity):
        print('Spending again aren\'t you?')
        return super().withdraw(quantity)