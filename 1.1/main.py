#
#
# Copyright 2014 Zola (AdeebNqo) Mahlaza
#
#
import sys, time
from daemon3x import daemon 

import pyinotify
import subprocess
from mmutil import *
import argparse

watchedfolders = []

#class to listen to folders
class music_manager(daemon, pyinotify.ProcessEvent):
        def run(self):
		#object for handling the events sent by the actions which will be monitored
		event_handler = self #EventHandler()
		watch_manager = pyinotify.WatchManager()
		#actions to watch for in the assigned golder
		actions = pyinotify.IN_MOVED_TO | pyinotify.IN_CLOSE_WRITE | pyinotify.IN_CLOSE_NOWRITE
		notifier = pyinotify.Notifier(watch_manager, event_handler)
		#adding folder to monitor
		for folder in watchedfolders:
			watch_manager.add_watch(folder, actions)
                while True:
                        #time.sleep(10)
			notifier.process_events()
			if (notifier.check_events()):
				notifier.read_events()

	def process_IN_CLOSE_WRITE(self,event):
		self.place(event.pathname)
	def process_IN_MOVED_TO(self,event):
		self.place(event.pathname)
	def ismusicfile(self, filepath):
		response = subprocess.Popen("file "+filepath, stdout=PIPE).stdout.read()
		if (response.split(':')[1].startswith(' Audio file ')):
			return True
		return False
	def place(self,filepath):
		if (self.ismusicfile(filepath)):
			song_classifier = classifier(musicfolder)
			fs = filesystem(musicfolder)
			path = song_classifier.classify(filepath, True)
			if (fs.file_exists(path)==False):
				fs.create_path(song_classifier.get_cached_artist(), song_classifier.get_cached_album())
			try:
				fs.move(filepath, path)
				return True
			except shutil.Error,err:
				return False

def main():
	parser = argparse.ArgumentParser(description='Deamon for managing music.')
	
	daemon = music_manager('/tmp/music_manager.pid')
	if len(sys.argv) == 2:
	        if 'start' == sys.argv[1]:
	                daemon.start()
	        elif 'stop' == sys.argv[1]:
	                daemon.stop()
	        elif 'restart' == sys.argv[1]:
	                daemon.restart()
	        else:
	                print "Unknown command"
	                sys.exit(2)
	        sys.exit(0)
	else:
	        print "usage: %s start|stop|restart" % sys.argv[0]
	        sys.exit(2)
if __name__=='__main__':
	main()
