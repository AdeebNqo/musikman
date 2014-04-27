
#
# This module is for making sure that when there are multiple
# file being added to a watched folder, the user is not bombaded
# with a billion notifications.
#
#
# Copyleft 2013 Zola Mahlaza (AdeebNqo) <adeebnqo@gmail.com>
#
#
import threading
import time
num = 0
class numCancellor(threading.Thread):
	def run(self):
		global num
		time.sleep(5000)
		num = 0
class user_notif(object):
	def __init__(self):
		self.thread_started = False
	def can_notify(self):
		global num
		if (num<3):
			return True
		elif (self.thread_started==False):
			mythread = numCancellor()
			mythread.start()
		return False
	def notify(self):
		global num
		num=num+1
