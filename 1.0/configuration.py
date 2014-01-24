#
#
# File for storing configuration into file
#
#
import pickle
write_configFile = open("config.pkl","w")
read_configFile = None
def init():
	read_configFile = open("config.pkl","r")

def save(configDictionary):
	pickle.dump(configDictionary, configFile)

def closeSaving():
	configFile.close()

#
#Infficient method for retrieving settings
#
def get(key):
	if (read_configFile!=None):
		cDict = pickle.load(read_configFile)
		return cDick[key]
	else:
		return None