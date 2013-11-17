class value(object):
	def __init__(self,name):
		self.length = len(name)
		self.stack = self.__split__(name)
		self.stack.reverse()
	def has_nexttoken(self):
		tmp_length = len(self.stack)
		if (tmp_length==0):
			return False
		return True
	def next_token(self):
		return self.stack.pop()
	def __split__(self, name):
		result = []
		for i in name:
			result.append(i)
		return result
class comparor(object):
	def __init__(self):
		self.similarity = 0
	#
	# Method for setting the left hand val
	# -Used when comparing val with multiple others-
	def set_leftartist(self,val0):
		self.val0 = val0
	#
	# Method for comparing val one with set artist
	# - Used when comparing val with multiple others-
	def compare(val1):
		compare(self.val0, val1)
	#
	# Method for comparing two vals
	#
	def compare(self, val0, val1):
		self.similarity = 0
		#
		# Comparing artists
		#
		tmpval0 = value(val0)
		tmpval1 = value(val1)
		
		atoken = tmpval0.next_token()
		btoken = tmpval1.next_token()
		num=0
		while(1):
			if (atoken!=" " and btoken!=" "):
				#we can compare
				if (atoken==btoken):
					num=num+1
					if (tmpval0.has_nexttoken()):
						atoken=tmpval0.next_token()
					else:
						break
					if (tmpval1.has_nexttoken()):
						btoken = tmpval1.next_token()
					else:
						break
				else:
					break
			else:
				#Need to ignore token
				if (atoken==" "):
					if (tmpval0.has_nexttoken()):
						atoken = tmpval0.next_token()
					else:
						break
				elif (btoken==" "):
					if (tmpval1.has_nexttoken()):
						btoken = tmpval1.next_token()
					else:
						break
		length = min(tmpval0.length, tmpval1.length)
		print("length: "+str(length))
		print("num: "+str(num))
		if (num==0):
			return 0
		else:
			num = 1.0 * num
			self.similarity = num/length
			return self.similarity*100
def main():
	print("Hello World")
	com = comparor()
	print(com.compare("Blackcoffee","Black Coffee"))
if __name__=="__main__":
	main()
