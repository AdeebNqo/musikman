from util import filesystem
from util import song
import os
def main():
	
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
			artist = (current_song.get_artist())
			album = current_song.get_album()
			fs.copy(current_file,"/tmp/.musikMan", artist, album, fs.file_index)
if __name__=="__main__":
	main()
