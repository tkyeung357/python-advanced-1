class Account_Exception (Exception):
	pass

class Bank():
	def __init__(self, id):
		self.__id = id
		self.__balance = 0

	@property
	def balance(self):
		return self.__balance
	
	@balance.setter
	def balance(self, balance):
		if balance < 0:
			raise Account_Exception("it should not be possible to set a negative balance")
		if abs(self.__balance - balance) > 100_000:
			print("auditing purposes")

		self.__balance = balance
	
	@property
	def id(self):
		return self.__id
	@id.setter
	def id(self):
		raise Account_Exception("not allow")
	@id.deleter
	def id(self):
		raise Account_Exception("not allow")
	def __str__(self):
		return ("account {} balance is {}".format(self.__id, self.__balance))

acc = Bank("id-123-123")
acc.balance += 1000
print(acc)
acc.balance += 100_000
print(acc)
acc.balance -= 100_001
print(acc)