
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

num = 0
class numCancellor(threading.Thread):
	def run(self):
		sleep(5000)
		num = 0
class user_notif(object):
	def __init__(self):
		num=0
	def can_notify(self):
		if (num<3):
			return True
		return False
	def notify(self):
		num=num+1
