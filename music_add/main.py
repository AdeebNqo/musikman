import sys
import pyinotify
#
# Class for handling events from inotify
#
class EventHandler(pyinotify.ProcessEvent):
	def __init__(self):
		self.tmp = 0
	def process_IN_CLOSE_WRITE(self,event):
		print('write')
	def process_IN_MOVED_TO(self,event):
		print('moved')	
def main():
	path = sys.argv[1]
	print('MusikMan: watching '+path)
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
		print('MusikMan: \'unwatching\' '+path)
		notifier.stop()
		print(err)
if __name__=='__main__':
	main()
		
