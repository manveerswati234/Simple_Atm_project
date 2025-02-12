# class atm:
#     def __init__(self):
#         self.balance=50000
#         self.pin=1234
#         self.attempt= 3
#     def authentication(self):
#         while self.attempt>0:
#             enter_pin= int(input("Enter your pin :"))
#             if self.pin==enter_pin:
#                 print("Your Pin is correct")
#                 return True
#             else:
#                 self.attempt -=1
#                 print(f"Your pin is incorrect {self.attempt}")
#         print("To many attempts you are exit")
#         return False
#     def check_balance(self):
#         print(f"Your account balance is {self.balance}")
#     def withdrawl(self):
#         amount= int(input("Enter your withdrawl amount"))
#         if amount<=0:
#             print("Entered a valid amount")
#         elif amount>self.balance:
#             print("Insufficent balance")
#         else:
#             self.balance -=amount
#             print(f"Successfully withdrawl {amount} and Your new balance is {self.balance}")
#     def deposit(self):
#         amount= int(input("Enter your amount you have deposit"))
#         if amount<=0:
#             print("Your Entered amount is invalid")
#         else:
#             self.balance +=amount
#             print(f"Successfully deposit {amount} and Your new balance is {self.balance}")
#     def exit(self):
#         print("Thank you for using the ATM. Goodbye!")
#     def run(self):
#         if not self.authentication():
#             return
#         while True:
#             print("/n ATM Menu :")
#             print("1- Check Balance")
#             print("2- Withdrawl money")
#             print("3- Deposit Money")
#             print("4- Exit")
#             operation= int(input("Enter your Choice : "))
#             if operation==1:
#                 self.check_balance()
#             elif operation==2:
#                 self.withdrawl()
#             elif operation == 3:sfu
#                 self.deposit()
#             elif operation == 4:
#                 self.exit()
#                 break
#             else:
#                 print("Invalid Choice")
# Atm= atm()
# Atm.run()

class atm:
    def __init__(self):
        self.pin= 1234
        self.balance= 50000
        self.attempts=3
    def authenticate(self):
        while self.attempts>0:
            enter_pin= int(input("Enter your pin number -"))
            if enter_pin==self.pin:
                print("Your Authentication is succesfully")
                return True
            else:
                self.attempts -=1
                print("Your Pin number is invalid")
        print("Many attempts you are exit")
        return False
    def check_balance(self):
        print(f"Your Balance is {self.balance}")
    def withdrawl(self):
        enetr_amount= int(input("Enter your amount -"))
        if enetr_amount<=0:
            print("Please enter a valid amount")
        elif enetr_amount>self.balance:
            print("Your balance is insufficent")
        else:
            self.balance -=enetr_amount
            print(f"Your withdrawl balance is {enetr_amount} and account balance is {self.balance}")
    def deposit(self):
        enetr_amount= int(input("Enter your amount -"))
        if enetr_amount<=0:
            print("Please enter a valid amount")
        else:
            self.balance += enetr_amount
            print(f"Your deposit amount is {enetr_amount} and account balance is {self.balance}")
    def exit(self):
        print("Thank you for using the ATM. Good Bye____")
    def run(self):
        if not self.authenticate():
            return
        while True:
            print("/n ATM Menu :")
            print("1- Check Balance")
            print("2- Withdrawl money")
            print("3- Deposit Money")
            print("4- Exit")
            operation= int(input("Enter your Choice -"))
            if operation==1:
                self.check_balance()
            elif operation==2:
                self.withdrawl()
            elif operation==3:
                self.deposit()
            elif operation==4:
                self.exit()
            else:
                print("Invalid Choice. Sorry!")
Atm= atm()
Atm.run()
 
            
            
             




