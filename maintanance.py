class value(object):
	def __init__(self,name):
		self.length = len(name)
		self.stack = self.__split__(name)
		self.stack.reverse()
	def next_token(self):
		return self.stack.pop()
	def __split__(self, name):
		result = []
		for i in name:
			result.append(i)
		return result
