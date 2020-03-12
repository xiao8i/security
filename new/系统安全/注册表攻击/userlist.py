from _winreg import *
import sys


"""注册表获取用户账户"""
reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE) #  搜索根键目录
subreg = "SOFTWARE\\Microsoft\\windows NT\\CurrentVersion\\ProfileList"
key = OpenKey(reg, subreg) #  获取注册表项
for i in range(1024):
	try:
		subkey = Enumkey(key, i) # z注册表项下的子健
		subreg2 = "%s\\%s" % (subreg, subkey) #  子键目录
		subkey2 = OpenKey(reg, subreg2) #  获取子键
		try:
			for j in range(1024):
				n, v, t = EnumValue(subkey2, j) #  获取第j条记录，对应项”名称，类型，数据“
				if ("ProfileImagePath" in n and "User" in v):
					print(v) #  v保存用户名
		except:
			errorMsg = "Exception Inner:", sys.exc_info()[0]
			print(errorMsg)
		CloseKey(subkey2)
	except:
		errorMsg = "Exception Outter:", sys.exc_info()[0]
		break
CloseKey(key)
CloseKey(reg)