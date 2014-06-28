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
from os.path import expanduser
import os.path

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
		p = subprocess.Popen(['file',filepath], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		response, err = p.communicate()
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

	#reading saved folders which need to be watched
	configpath = expanduser("~")+'/.musicman/config'
	if not os.path.exists(os.path.dirname(configpath)):
		os.makedirs(os.path.dirname(configpath))
	if (not os.path.isfile(configpath)):
		open(configpath,'a').close()
	configfile = open(configpath,'r+')
	for line in configfile.readlines():
		watchedfolders.append(line)
	#getting cmdline args
	parser = argparse.ArgumentParser(description='Deamon for managing music.')
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('-f','--folder', nargs='+', help='Path of folder to watch for deamon to watch', required=False)
	group.add_argument('-s','--status',  help='Control deamon. Start, stop or restart it', required=False)
	group.add_argument('-p','--process',  help='Manage music in specified folder', required=False)
	args = vars(parser.parse_args())
	#processing provided folder
	if (args['process']!=None):
		folder = args['process']
		#editing folder path incase it's a relative path
		if (not os.path.isabs(folder)):
			folder = os.path.abspath(folder)
		tmp = music_manager('/tmp/tmp.pid') #deamon will not be started
		print('processing...')
		#iterating through all files in folder
		for root, _, files in os.walk(folder):
		    for f in files:
			fullpath = os.path.join(root, f)
			if tmp.ismusicfile(fullpath):
				tmp.place(fullpath)
		print('done')
		
	#processing new passed folders if there are any
	if (args['folder']!=None):
		newfolders = args['folder']
		config = open(configpath)
		for folder in newfolders:
			#editing folder path incase it's a relative path
			if (not os.path.isabs(folder)):
				folder = os.path.abspath(folder)
			watchedfolders.append(folder)
			configfile.write(folder)
			configfile.write('\n')
	configfile.close()
	#checking status of deamon if requested
	if (args['status']!=None):
		status = args['status'].lower();
		daemon = music_manager('/tmp/music_manager.pid')
	        if 'start' == status:
	                daemon.start()
	        elif 'stop' == status:
	                daemon.stop()
	        elif 'restart' == status:
	                daemon.restart()
	        else:
	                print "Unknown command"
	                sys.exit(2)
	        sys.exit(0)

if __name__=='__main__':
	main()
