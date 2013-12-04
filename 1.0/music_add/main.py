#
#
# This module is the entry point to the program
# It contains some utility functions that need not be created in sepe
#
# Copyleft 2013 Zola Mahlaza (AdeebNqo) <adeebnqo@gmail.com>
#

import sys
import pyinotify
from mmutil import *
from config import config
from user_notif import user_notif
from notifications import notification

configuration = config() #object for reading saved configuration
musicfolder = configuration.get('music folder').replace('\n','') 
notifications = configuration.get('notifications').replace('\n','')

unotif = user_notif() #object for controlling notification of moved music file

#
#setting up notification system
#
if (notifications=='True'):
	notif = notification()
else:
	notif = None
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
def ismusicfile(filepath):
	if filepath.endswith('.mp3'):
		return True
	elif filepath.endswith('.wma'):
		return True
	print('ignored '+filepath)
	return False
#
# Method for placing, that is, moving a file to it's allocated folder on the music folder
#
def place(filepath):
	print('processing '+filepath)
	if ismusicfile(filepath):
		song_classifier = classifier(musicfolder)
		fs = filesystem(musicfolder)
		path = song_classifier.classify(filepath, True)
		if (fs.file_exists(path)==False):
			fs.create_path(song_classifier.get_cached_artist(), song_classifier.get_cached_album())
		try:
			fs.move(filepath, path)
			print('placed '+song_classifier.get_cached_artist()+'\'s song in '+path)
			if (unotif.can_notify()):
				unotif.notify()
				notif.notify('placed '+song_classifier.get_cached_artist()+'\'s song in '+path)
		except shutil.Error,err:
			if (unotif.can_notify()):
				unotif.notify()
				notif.notify('Duplicate file ignored')
			else:
				print('Duplicate file ignored')
			
			
def main():
	path = sys.argv[1]
	#Notifying user that chosen folder is being watched
	if (notifications=='True'):
		notif.notify('watching '+path)
	else:
		print('watching '+path)
	#object for handling the events sent by the actions which will be monitored
	event_handler = EventHandler()
	watch_manager = pyinotify.WatchManager()
	#actions to watch for in the assigned golder
	actions = pyinotify.IN_MOVED_TO | pyinotify.IN_CLOSE_WRITE | pyinotify.IN_CLOSE_NOWRITE
	notifier = pyinotify.Notifier(watch_manager, event_handler)
	
	watch_manager.add_watch(path, actions)
	try:
		while True:
			notifier.process_events()
			if (notifier.check_events()):
				notifier.read_events()
	except Exception,err:
		notifier.stop()
		if (notifications=='True'):
			notif.notify('un-watching '+path)
		else:
			print('un-watching '+path)
		print(err)
if __name__=='__main__':
	main()
		
