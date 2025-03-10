"""
ATM Machine Implementation using Object-Oriented Programming in Python.
This script allows users to:
1. Create a PIN
2. Deposit money
3. Withdraw money
4. Check balance
5. Exit

Encapsulation is used to secure balance and PIN data.
"""

class Atm:
    """Class representing an ATM machine."""
    
    def __init__(self):
        """Constructor to initialize PIN and balance, and call the menu."""
        self.__pin = ""  # Private variable for security
        self.__balance = 0  # Private variable to store balance
        self.menu()
    
    def menu(self):
        """Displays the menu and processes user input."""
        user_input = input("""
        Hello, how would you like to proceed?
        1. Enter 1 to create PIN
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to exit
        """)
        
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.check_balance()
        elif user_input == '5':
            print("Thank you for using the ATM. Goodbye!")
            exit()
        else:
            print("Invalid choice! Try again.")
            self.menu()
    
    def create_pin(self):
        """Allows user to set a new PIN."""
        self.__pin = input("Enter your new PIN: ")
        print("PIN set successfully.")
        self.menu()
    
    def deposit(self):
        """Deposits money into the account after verifying the PIN."""
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.__pin:
            amount = int(input("Enter deposit amount: "))
            self.__balance += amount
            print("Amount deposited successfully.")
        else:
            print("Incorrect PIN.")
        self.menu()
    
    def withdraw(self):
        """Withdraws money after verifying the PIN and checking balance."""
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.__pin:
            amount = int(input("Enter withdrawal amount: "))
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient balance.")
        else:
            print("Incorrect PIN.")
        self.menu()
    
    def check_balance(self):
        """Checks and displays account balance after PIN verification."""
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.__pin:
            print(f"Your balance is {self.__balance}.")
        else:
            print("Incorrect PIN.")
        self.menu()

# Creating an ATM object to start the application
atm = Atm()
