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
	#
	# Method for logging sessions errors
	#
	def report_error(self, File, error):
		issue = Issue(File,error)
		self.session_errors.append(issue)
	#
	# Method for quick reporting of errors
	# Must be use when there are a few errors
	#
	def qreport_error(self,File,error):
		f = open(self.log_file,"w")
		f.write(time.ctime()+": "+issue.File+", "+issue.error.__str__()+"\n")
		f.write("\n")
		f.close()	
	def close(self):
		f = open(self.log_file,"w")
		for issue in self.session_errors:
			f.write(time.ctime()+": "+issue.File+", "+issue.error.__str__()+"\n")
		f.write("\n")
		f.close()
