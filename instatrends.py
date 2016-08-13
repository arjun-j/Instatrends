import os
import sys
from googlemaps import *
from inst_api import *


def main():
	#Argument sanity check
	if(len(sys.argv) != 4 ):
		print "Usage : ", sys.argv[0], "<lat> <long> <distance>"
		sys.exit(1)
	
	#crerate object of class API
	loc_point = API(sys.argv[1], sys.argv[2], sys.argv[3])

	#get the requuired media data and stre in JSON file
	loc_point.get_data()

	#run map local server
	flask_server.app.run(debug=True)

if __name__ == '__main__':
	main()
