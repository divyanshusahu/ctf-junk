#!/usr/bin/python2.7
import zipfile
import optparse
import os
from threading import Thread

def crackpass(filename, password) :
	try :
		filename.extractall(pwd=password)
		print "[+] Password Found :" + password
		os._exit(0)
	except :
		pass

def main() :
	parser = optparse.OptionParser()
	parser.add_option('-f', '--file', help="Zip File to crack (required)", dest="fname")
	parser.add_option('-d', '--dict', help="Dictionary file to crack password (required)", dest="dict")

	(options, args) = parser.parse_args()

	mandatory = ["fname", "dict"]
	for m in mandatory :
		if options.__dict__[m] == None :
			print "[+] Mandatory options are missing"
			print parser.print_help()
			exit(-1)

	filename = options.fname
	dictionary = options.dict

	try :
		file = zipfile.ZipFile(filename)
		with open(dictionary, 'r') as dictny :
			passwords = dictny.readlines()

		for password in passwords :
			password = password.strip('\n')
			t = Thread(target=crackpass, args=(file, password))
			t.daemon = True
			t.start()
	
	except Exception, e :
		print e
		exit(-1)

if __name__ == '__main__':
	main()