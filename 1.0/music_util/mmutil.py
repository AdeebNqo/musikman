import os
class song(object):
	def __init__(self, path):
		try:
			f = open(path)
			f.seek(-128,os.SEEK_END)
			tag = f.read(3)
			if (tag=="TAG"):
				self.title = f.read(30)
				self.artist = self.__sanitize__(f.read(30))
				self.album = self.__sanitize__(f.read(30))
				if (self.artist==""):
					self.__unknown__()
				elif (self.album==""):
					self.album="Unknown"
				self.year = f.read(4)
			else:
				self.__unknown__()
			##atist and album are empty
		except IOError:
			self.title = "Unknown"
			self.artist = "Unknown"
			self.album = "Unknown"
			self.year = "Unknown"
			print("log: "+path)
	def get_artist(self):
		return self.artist
	def get_album(self):
		return self.album
	def __sanitize__(self,name):
		return name.strip("\x00")
	def __unknown__(self):
		self.title = "Unknown"
		self.artist = "Unknown"
		self.album = "Unknown"
		self.year = "Unknown"

#Class for classfying songs
class classifier(object):
	def __init__(self, music_folder):
		self.music_folder = music_folder
	#
	# Method for classfying a song
	# song_path : path to music file
	# cache : boolean value for deciding to cache the song details
	def classify(song_path, cache):
		song = song(song_path)
		artist = song.get_artist()
		album = song.get_album()
		if (cache):
			self.artist = artist
			self.album = album
		else:
			self.artist =None
			self.album = None
		path = music_folder+'/'+artist+'/'+album		
		return path
	def get_cached_artist(self):
		return self.artist
	def get_cached_album(self):
		return self.album

#
#Class for dealing with the file system
#
class filesystem(object):
	def __init__(self,topdir):
		self.topdir = topdir
	def file_xists(self,path):
		return os.path.exists(folder_path)
	def create_path(self, artist, album):
		artist_path = topdir+"/"+artist
		album_path = topdir+"/"+artist+"/"+album
		if (self.file_exists(artist_path)):
				#Artist dir exists
				if (self.file_exists(album_path)):
					#album folder exists
					return
				else:
					#album folder does not exist
					self.create_folder(album_path)
		else:
			#artist folder does not exist
			self.create_folder(album_path)


#
#----------------------------------------------------------------------
# The following class are to be used when comparing folders or artists
#----------------------------------------------------------------------
#
class value(object):
	def __init__(self,name):
		name = name.upper()
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
		print(result)
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
			if (atoken!=' ' and btoken!=' '):
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
				if (atoken==' '):
					if (tmpval0.has_nexttoken()):
						atoken = tmpval0.next_token()
					else:
						break
				elif (btoken==' '):
					if (tmpval1.has_nexttoken()):
						btoken = tmpval1.next_token()
					else:
						break
		length = min(tmpval0.length, tmpval1.length)
		if (num==0):
			return 0
		else:
			num = 1.0 * num
			self.similarity = num/length
			return self.similarity*100
#
# The following classes are for assisting with
# storing the generated folder
#
class folder(object):
	def __init__(self,path):
		self.path = path
		self.subdirectories = []
		#Retrieve subdirectories
		#...
		for dirnames in os.walk(path):
			subdirectories.append(dirnames[0])
	#
	# Method for joing given path
	# with current folder.
	#
	def join(self, path):
		#...
		print('join() called')
