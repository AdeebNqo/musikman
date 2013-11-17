import os
import shutil
import logger
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
		return name.replace("\x00","")
	def __unknown__(self):
		self.title = "Unknown"
		self.artist = "Unknown"
		self.album = "Unknown"
		self.year = "Unknown"
class filesystem(object):
	def __init__(self, topdir):
		self.file_index = 0
		self.folder_stack = []
		self.file_stack = []
		self.clearfile_stack=[]
		self.recurse(topdir)
		self.filestack_size = len(self.file_stack)
		self.log = logger.logger()
	def recurse(self, directory):
		for dirpath,dirnames,filenames in os.walk(directory):
			self.folder_stack.append(dirpath)
			for File in filenames:
				self.clearfile_stack.append(File)
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
	def copy(self, srcpath, destpath, artist, album, fileindex):
		print("Copying...")
		#		
		#creating directory that will contain file
		#
		artist_path = destpath+"/"+artist
		album_path = destpath+"/"+artist+"/"+album
		try:
			if (self.file_exists(artist_path)):
				#Artist dir exists
				if (self.file_exists(album_path)):
					#album folder exists
					f = self.clearfile_stack[fileindex]
					if (self.file_exists(album_path+"/"+f)):
						#file already exists						
						return
				else:
					#album folder does not exist
					self.create_folder(album_path)
			else:
				#artist folder does not exist
				self.create_folder(album_path)
			#Copying file
			try:
				shutil.copy(srcpath, album_path)
				print("copied!")
			except IOError as error0:
				print("Copy failed!")
				self.log.report_error(srcpath, error0)
		except TypeError as error:
			print("Copy failed!")
			self.log.report_error(srcpath,error)

	def file_exists(self, folder_path):
		return os.path.exists(folder_path)
	def create_folder(self, folder_path):
		os.makedirs(folder_path)
	def move(self, path, destpath, artist, album):
		print("Moving...")
	#
	# Method for releasing all acquired resources, cleaning up, etc
	#
	def release(self):
		self.log.close()
