from util import filesystem
from util import song
import os
def main():
	while(True):
		print("\t/--Options--/")
		print()
		print("Enter cmd:")
	#Creating temp directory to contain music
	if (os.path.exists("/tmp/.musikMan")):
		try:
			os.removedirs("/tmp/.musikMan")
			os.makedirs("/tmp/.musikMan");
		except OSError:
			print("log: cannot delete tmp dir") 
	else:
		os.makedirs("/tmp/.musikMan");
	#reading music folder
	fs = filesystem("/home/adeeb/Music")
	while(fs.has_nextfile()):
		current_file = fs.nextfile()
		if (current_file!=None):
			current_song = song(current_file)
			artist = current_song.get_artist()
			album = current_song.get_album()
			fs.pcopy(current_file,"/tmp/.musikMan", artist, album, fs.file_index)
	fs.release()
if __name__=="__main__":
	main()
