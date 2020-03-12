from _winreg import *
import sys


"""注册表修改防火墙设置"""
try:
	reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
	subreg = "SYSTEM\\CurrentControlSet\\services\\SharedAccess\\Parameters\\Firewallpolicy"
	key = CreateKey(reg, subreg + "\\StandardProfile") #  内部网络
	SetValueEX(key, "EnableFirewall", 0, REG_DWORD, 0) #  0表示禁用防火墙。双字型
	CloseKey(key)
	key = CreateKey(reg, subreg + "\\PublicProfile") #  公用网络
	SetValueEX(key, "EnableFirewall", 0, REG_DWORD, 0) #  0表示禁用防火墙。双字型
except:
	errorMsg = "Exception Outter:", sys.exc_info()[0]
	print(errorMsg)
CloseKey(key)
CloseKey(reg)