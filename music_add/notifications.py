#
# Z. Mahlaza
# Class for notifying when device  detected
#
import pynotify
class notification:
	#
	# Notification types
	#
	info = "dialog-information"
	
	def __init__(self):
		self.title = "Music Management"
	def notify(self, msg):
		pynotify.init(self.title)
		notif = pynotify.Notification("Hello World", 'Hello World', )
		notif.show()
