class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner            # public attribute
        self.__balance = balance      # private attribute (name-mangled)

    # ---------- Deposit ----------
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"Deposited ${amount}. New balance: ${self.__balance}")

    # ---------- Withdraw ----------
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.__balance:
            print("Insufficient funds.")
            return
        self.__balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.__balance}")

    # ---------- Display balance ----------
    def get_balance(self):
        return self.__balance

    def display_balance(self):
        print(f"{self.owner}'s current balance: ${self.__balance}")


# ------------------- Demonstration -------------------
account = BankAccount("Alice", 1000)

account.display_balance()      # Alice's current balance: $1000

account.deposit(500)           # Deposited $500. New balance: $1500
account.withdraw(200)          # Withdrew $200. New balance: $1300
account.withdraw(5000)         # Insufficient funds.
account.deposit(-50)           # Deposit amount must be positive.

account.display_balance()      # Alice's current balance: $1300

# ---- Trying to access the private attribute directly ----
try:
    print(account.__balance)
except AttributeError as e:
    print(f"Error: {e}")

# Direct access fails because of name mangling, but this "backdoor" still works:
print(account._BankAccount__balance)   # $1300 — shows it's not truly unbreakable
