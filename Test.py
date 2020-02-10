from atm import *

base = BaseATM(30)
base.deposit(30)
base.withdraw(12)
base.check_balance()

coach = CoachATM(50)
coach.deposit(5)

shark = LoanSharkATM(10)
shark.withdraw(30)# should be -35
shark.withdraw(30)# should be -95

snarky = SnarkyATM(50)
snarky.deposit(10)
snarky.withdraw(10)