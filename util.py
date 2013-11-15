import os
import shutil
class song(object):
	def __init__(self, path):
		try:
			f = open(path)
			f.seek(-128,os.SEEK_END)
			tag = f.read(3)
			if (tag=="TAG"):
				self.title = f.read(30)
				self.artist = f.read(30)
				self.album = f.read(30)
				self.year = f.read(4)
			else:
				self.title = "Unknown"
				self.artist = "Unknown"
				self.album = "Unknown"
				self.year = "Unknown"
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
class filesystem(object):
	def __init__(self, topdir):
		self.file_index = 0
		self.folder_stack = []
		self.file_stack = []
		self.recurse(topdir)
		self.filestack_size = len(self.file_stack)
	def recurse(self, directory):
		for dirpath,dirnames,filenames in os.walk(directory):
			self.folder_stack.append(dirpath)
			for File in filenames:
				self.file_stack.append(dirpath+"/"+File)
	def nextfile(self):
		self.file_index = self.file_index +1
		if (self.file_index>=self.filestack_size):
			return None
		else:
			return self.file_stack[self.file_index]
	def has_nextfile(self):
		if ((self.file_index>=self.filestack_size)):
			return False
		else:
			return True
	def copy(self, srcpath, destpath, artist, album):
		print("Copying...")
		#creating directory that will contain file		
		if (os.path.exists(destpath+"/"+artist)):
			if (os.path.exists(destpath+"/"+artist+"/"+album)==False):
				os.makedirs(destpath+"/"+artist+"/"+album)
		else:
			os.makedirs(destpath+"/"+artist+"/"+album)
		#Copying file
		shutil.copy(srcpath, destpath+"/"+artist+"/"+album)
		print("copied!")
				
	def move(self, path, destpath, artist, album):
		print("Moving...")
