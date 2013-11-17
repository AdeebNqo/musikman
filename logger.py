import time
class Issue(object):
	def __init__(self, File, error):
		self.File = File
		self.error = error
	def get_file(self):
		return self.File
	def get_error(self):
		return self.error
class logger(object):
	def __init__(self):
		self.log_file="/tmp/.musikMan_log"
		self.session_errors = []
	def report_error(self, File, error):
		issue = Issue(File,error)
		self.session_errors.append(issue)
	def close(self):
		f = open(self.log_file,"w")
		for issue in self.session_errors:
			f.write(time.ctime()+" File: "+issue.File+" Error: "+issue.error.__str__()+"\n")
		f.close()
