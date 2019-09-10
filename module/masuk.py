#System Login

blue = '\033[34;1m'
green = '\033[32;1m'
purple = '\033[35;1m'
cyan = '\033[36;1m'
red = '\033[31;1m'
white = '\033[37;1m'
yellow = '\033[33;1m'

import os, sys

print "\033[32;1m   _______                             "
print "\033[32;1m  (       )                            "
print "\033[32;1m  | [] [] |    \033[37;1mHii,          "
print "\033[32;1m  |   _   |    \033[37;1mWelcome To My "
print "\033[32;1m _(_______)_   \033[37;1mProject :)    "
print "\033[32;1m(    \ /    )                          "
print "\033[32;1m| (   |   ) |                          "
print "\033[32;1m| |   .   | |   \033[31;1mMr.yM        "
print "\033[32;1m| |   .   | |                          "
print "\033[32;1m|_(_______)_|                          "
print
print ("\033[32;1mMasukan Username dan Password !")
print ("\033[36;1mKalo Gak Tau liat di Readme")
username = 'Maulanarym'      
password = 'subscribe'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("\033[37;1musername : ")
	if uname == username:
		pwd = raw_input("\033[31;1mpassword : ")

		if pwd == password:
			print "\033[37;1mHello Welcome To My Tools"
			print "\033[34;1mDon't Copy My Project !",
			sys.exit()

		else:
			print "\033[31;1mPassword Kamu Salah!!!"
			print "\033[37;1mBack Login"
			restart()

	else:
		print "\033[31;1mUsername Kamu Salah !!!"
		print "\033[37;1mBack Login"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()