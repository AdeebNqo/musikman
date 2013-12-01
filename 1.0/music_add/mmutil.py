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
	def classify(self,song_path, cache):
		currentsong = song(song_path)
		artist = currentsong.get_artist()
		album = currentsong.get_album()
		if (cache):
			self.artist = artist
			self.album = album
		else:
			self.artist =None
			self.album = None
		path = self.music_folder+'/'+artist+'/'+album		
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
	def file_exists(self,path):
		return os.path.exists(path)
	def create_path(self, artist, album):
		artist_path = self.topdir+"/"+artist
		album_path = self.topdir+"/"+artist+"/"+album
		if (self.file_exists(artist_path)):
				#Artist dir exists
				if (self.file_exists(album_path)):
					#album folder exists
					return False
				else:
					#album folder does not exist
					self.create_folder(album_path)
					return True
		else:
			#artist folder does not exist
			self.create_folder(album_path)
			return True
	def move(self, srcpath, destpath):
		shutil.move(srcpath, destpath)
	def create_folder(self, folder_path):
		os.makedirs(folder_path)
