class bankaccount:
  def __init__(self,account_number,holder_name,initial_balance):
    self.account_number = account_number
    self._holder_name = holder_name
    self.__balance = initial_balance

  def deposit(self ,amount):
    if amount > 0 :
      self.__balance += amount
      print(f"{amount} deposited. New balance: {self.__balance}")
    else:
      print("Invalid deposit amount")

  def withdraw(self , amount):
    if 0 < amount <= self.__balance:
      self.__balance -= amount
      print(f"{amount} withdraw . remaning balance : {self.__balance}")

  def get_balance(self):
    return self.__balance

  def _display_holder(self):
    print(f"account holder : {self._holder_name}")


# subclass with limited access to parent class menbers

class savingaccount(bankaccount):
  def __init__(self , account_number,holder_name,initial_balance , interest_rate):
    super().__init__( account_number , holder_name , initial_balance )
    self.interest_rate = interest_rate  #public

  def apply_interest(self):
    interest = self.get_balance() * (self.interest_rate / 100)
    print(f"applying interest : {interest}")

  def display_info(self):
    self._display_holder()  # accessing protected method
    print(f"account number : {self.account_number}")
    print(f"balance : {self.get_balance()}")
    print(f"interest rate : {self.interest_rate}%")



acc = savingaccount(123456789 , "Dewansh" , 5000,7)
acc.display_info()
