import sys
import pyinotify
from mmutil import *
from config import config

configuration = config()
music_folder = configuration.get('music folder').replace('\n','')
#
# Class for handling events from inotify
#
class EventHandler(pyinotify.ProcessEvent):
	def __init__(self):
		self.tmp = 0
	def process_IN_CLOSE_WRITE(self,event):
		place(event.pathname)
	def process_IN_MOVED_TO(self,event):
		place(event.pathname)
def place(filepath):
	song_classifier = classifier(music_folder)
	fs = filesystem(music_folder)
	path = song_classifier.classify(filepath, True)
	if not fs.file_exists(path):
		fs.create_path(path)
	fs.move(filepath, path)
	print('placed '+song_classifier.get_cachedartist()+'\'s song in '+path)
def main():
	path = sys.argv[1]
	print('musikman: watching '+path)
	event_handler = EventHandler()
	watch_manager = pyinotify.WatchManager()
	actions = pyinotify.IN_MOVED_TO | pyinotify.IN_CLOSE_WRITE | pyinotify.IN_CLOSE_NOWRITE
	notifier = pyinotify.Notifier(watch_manager, event_handler)
	
	watch_manager.add_watch(path, actions)
	try:
		while True:
			notifier.process_events()
			if (notifier.check_events()):
				notifier.read_events()
	except Exception as err:
		print('musikman: \'unwatching\' '+path)
		notifier.stop()
		print(err)
if __name__=='__main__':
	main()
		
