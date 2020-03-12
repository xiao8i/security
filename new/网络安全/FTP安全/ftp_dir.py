from ftplib import FTP 


"""ftp获取服务器目录"""
apache_dir = "htdocs"
server_name = "server"
server_id = "id"
server_pw = "password"


def getdir(cftp, name):
	#  获取目录	
	list = []
	if ("." not in name): #  .扩展名 为文件
		if (len(name) == 0):
			list = ftp.nlst()
		else:
			list = ftp.nlst(name)
			pass
	return list


def check(dir1, dir2):
	#  检查是否为目标目录
	if (dir1.lower().find(apache_dir) >= 0):
		print(dir1)
	if (dir2.lower().find(apache_dir) >= 0):
		print(dir1 + "/" + dir2)


ftp = FTP(server_name, server_id, server_pw)
dir1 = getdir(ftp, "") #  从根目录开始
for name1 in dir1:
	check(name1, "")
	dir2 = getdir(ftp, name1)
	for name2 in dir2:
		check(name1, name2)
		dir3 = getdir(ftp, name1 + "/" + name2)