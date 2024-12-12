class InMemoryDatabase:
	def __init__(self):
		self.data = {}
		self.transaction_stack = {}
		self.transaction_inprogress = False

	def begin_transaction(self):
		self.transaction_inprogress = True

	def get(self, key):
		return self.data.get(key, None)
	
	def put(self, key, value):
		if self.transaction_inprogress:
			self.transaction_stack[key] = value
		else:
			raise Exception("No transaction in progress.")

	def rollback(self):
		if self.transaction_inprogress:
			self.transaction_stack.clear()
			self.transaction_inprogress = False
		else:
			raise Exception("No transaction to rollback.")

	def commit(self):
		if self.transaction_inprogress:
			for key, value in self.transaction_stack.items():
				self.data[key] = value
			self.transaction_stack.clear()
			self.transaction_inprogress = False
		else:
			raise Exception("No transaction to commit.")
