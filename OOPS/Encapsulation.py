class BankAccount:
	def __init__(self,balance):
		self.__balance = balance
		
	def get_balance(self):
		return self.__balance
		
	def deposit(self,amount):
		self.__balance+=amount
		
	def withdraw(self,amount):
		if self.__balance>=amount:
			self.__balance-=amount
		else:
			print("Insufficient Balance")
	
account = BankAccount(1000)
print(account.get_balance())
account.deposit(500)
print(account.get_balance())
account.withdraw(2000)
print(account.get_balance())
