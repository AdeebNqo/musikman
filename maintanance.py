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
	# Method for setting the left hand artist
	# -Used when comparing artist with multiple others-
	def set_leftartist(self,artist0):
		self.artist0 = artist0
	#
	# Method for comparing artist1 one with set artist
	# - Used when comparing artist with multiple others-
	def compare(artist1):
		compare(self.artist0, artist1)
	#
	# Method for comparing two artists
	#
	def compare(self, artist0, artist1):
		self.similarity = 0
		#
		# Comparing artists
		#
		val0 = value(artist0)
		val1 = value(artist1)
		
		atoken = val0.next_token()
		btoken = val1.next_token()
		num=0
		while(1):
			if (atoken!=" " and btoken!=" "):
				#we can compare
				if (atoken==btoken):
					num=num+1
				else:
					break
			else:
				#Need to ignore token
				if (atoken==" "):
					if (val0.has_nexttoken()):
						atoken = val0.next_token()
					else:
						break
				elif (btoken==" "):
					if (val1.has_nexttoken()):
						btoken = val1.next_token()
					else:
						break
		length = min(val0.length, val1.length)
		if (num==0):
			return 0
		else:
			num = 1.0 * num
			self.similarity = length/num
			return self.similarity
	def 
