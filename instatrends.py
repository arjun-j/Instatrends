import os
import sys
from googlemaps import *
from inst_api import *


def main():
	#Argument sanity check
	if(len(sys.argv) != 4 ):
		print "Usage : ", sys.argv[0], "<lat> <long> <distance>"
		sys.exit(1)
	args = sys.argv	
	#crerate object of class API
	loc_point = API(args[1], args[2], args[3])

	#get the requuired media data and stre in JSON file
	loc_point.run()

	#run map local server
	flask_server.app.run(debug=True)

if __name__ == '__main__':
	main()
