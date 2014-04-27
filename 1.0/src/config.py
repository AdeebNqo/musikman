#
# Class for loading and saving configurations
#
class config(object):
	def __init__(self,configfile='config.mm'):
		self.configfile = configfile
		self.settings ={}
		#reading in sessions configuration
		f = open(configfile)
		lines = f.readlines()
		for line in lines:
			setting = line.split('=')
			self.settings[setting[0]] = setting[1]
	def get(self,config_field):
		return self.settings[config_field]
