from enum import Enum

class AccountType(Enum):
  SAVINGS = 1
  CHECKING = 2

class TransactionType(Enum):
  CREATE = 1
  BALANCE = 2
  DEPOSIT = 3
  WITHDRAW = 4

class BankAccount():
  def __init__(self, owner, accountType):
    """ Intializes a bank account for given type and owner
    """
    # Check if AccountType is an instance of class AccountType
    if not isinstance(accountType, AccountType):
      raise Exception("accountType has to be an instance of AccountType")

    self.owner = str(owner)
    self.accountType = accountType
    self.balance = 0

  def withdraw(self, amount):
    """ Withdraws specified amount from the account
    """
    # If there is not enough balance, print error
    if self.balance < amount:
      print("ERROR: You have not enough balance")
    else:
      self.balance = self.balance - amount

  def deposit(self, amount):
    """ Desposits specified amount to the account
    """
    self.balance = self.balance + amount

  def __str__(self):
    """ Returns an informative string of the account owner and the type of account
    """
    return f"The account owner is {self.owner}, and the type of the account is {self.accountType.name}"

  def __len__(self):
    """ Returns the balance of the account
    """
    return self.balance

class BankUser():
  def __init__(self, owner):
    """ Initializes a bank user
    """
    self.owner = owner
    self.accounts = {}

  def addAccount(self, accountType):
    """ Adds a new account to the user of the accountType specified.
        Only one savings/checking account per user.
    """
    # Check if accountType already exists for user
    if accountType in self.accounts:
      print(f"There already exists a {accountType.name} account")
    else:
      self.accounts[accountType] = BankAccount(self.owner, accountType)

  def getBalance(self, accountType):
    """ Get balance of given account
    """
    # Check if accountType exists for user
    if accountType not in self.accounts:
      print(f"There is no {accountType.name} account")
    else:
      print(f"Your {accountType.name} account has {len(self.accounts[accountType])}")

  def deposit(self, accountType, amount):
    """ Desposits specified amount to accountType
    """
    if accountType not in self.accounts:
      print(f"There is no {accountType.name} account")
    else:
      self.accounts[accountType].deposit(amount)

  def withdraw(self, accountType, amount):
    """ Withdraws specified amount from accountType
    """
    if accountType not in self.accounts:
      print(f"There is no {accountType.name}")
    else:
      self.accounts[accountType].withdraw(amount)

  def __str__(self):
    """ Returns an informative summary of user accounts
    """
    summary = ""
    if len(self.accounts) == 0:
      summary += f"{self.owner} has no accounts"
    else:
      summary += f"{self.owner} has {len(self.accounts)} accounts"
      for accountType, account in self.accounts.items():
       summary += f"\n {accountType.name} has balance of {len(account)}"
    return summary

# Class that keeps track of Session Info
class SessionInfo():
  def __init__(self, bankUser):
    self.transactionType = None
    self.accountType = None
    self.currentScreen = 1
    self.terminated = False
    self.bankUser = bankUser

  def __print_option_error(self):
    """ When option is not valid, print error
    """
    print("Not a valid input")

  def __reset_session(self):
    self.__init__(self.bankUser)

  def __screen_one(self, option):
    """ First Screen
        Input:
        option 1: Exit
        option 2: Create Account
        option 3: Check Balance
        option 4: Deposit
        option 5: Withdraw
    """
    if option == 1:
      self.terminated = True
    elif option in [2, 3, 4, 5]:
      # Note that TransactionType is enum starting at 1
      self.transactionType = TransactionType(option - 1)
      self.currentScreen = 2
    else:
      self.__print_option_error()

  def __screen_two(self, option):
    """ Second Screen
        Input:
        option 1: Checking
        option 2: Savings
    """
    if option in [1, 2]:
      # Note that AccountType Enum and Option order is different
      accountType = AccountType(3 - option)
      if self.transactionType.name == "CREATE":
        self.bankUser.addAccount(accountType)
        print(f"{accountType.name} Account has been created")
        self.__reset_session()
      elif self.transactionType.name == "BALANCE":
        self.bankUser.getBalance(accountType)
        self.__reset_session()
      elif self.transactionType.name in ["DEPOSIT", "WITHDRAW"]:
        self.accountType = accountType
        self.currentScreen = 3
    else:
      self.__print_option_error()

  def __screen_three(self, option):
    """ Third Screen
        option: should be positive integer
    """
    if self.transactionType.name == "DEPOSIT":
      self.bankUser.deposit(self.accountType, option)
      self.__reset_session()
    elif self.transactionType.name == "WITHDRAW":
      self.bankUser.withdraw(self.accountType, option)
      self.__reset_session()

  def proceed(self, option):
    """ Given user input option, proceed from the current screen
    """
    if self.currentScreen == 1:
      self.__screen_one(option)
    elif self.currentScreen == 2:
      self.__screen_two(option)
    elif self.currentScreen == 3:
      self.__screen_three(option)

  def check_terminated(self):
    return self.terminated

  def get_screen(self):
    return self.currentScreen

def ATMSession(bankUser):
  session = SessionInfo(bankUser)

  screenText = {
    1: "Enter Option:\n1)Exit\n2)Create Account\n3)Check Balance\n4)Deposit\n5)Withdraw\n",
    2: "Enter Option:\n1)Checking\n2)Savings\n",
    3: "Enter Integer Amount, Cannot Be Negative:"
  }

  def Interface():
    while not session.check_terminated():
      try:
        currentScreen = session.get_screen()
        option = int(input(screenText[currentScreen]))
        session.proceed(option)
      except (ValueError, TypeError):
        print("Input integers only")
  return Interface