import utils, sys
from pydbg import *
from pydbg.defines import *


#  pydbg模块实现API钩取，使得要保存到记事本数据"hate"变为"love"

"""
BOOL WINAPI WriteFile(
  _In_  HANDLE hFile,
  _In_  LPCVOID lpBuffer,
  _In_  DWORD nNumberOfBytesToWrite,
  _Out_opt_  LPDWORD lpNumberOfBytesWritten,
  _Inout_opt_  LPOVERLAPPED lpOverlapped
);
"""

dbg = pydbg()
isProcess = False
orgPattern = "hate"
repParrern = "love"
processName = "notepad.exe"


def replaceString(dbg, args): #  回调函数
	buffer = dbg.read_process_memory(args[1], args[2]) #  读取内存位置指定长度的值
	
	if orgPattern in buffer:
		print("Before is %s" % buffer)
		buffer=buffer.replace(orgPattern, repParrern) #  修改
		replace = dbg.write_process_memory(args[1], buffer) #  写入内存
		print("After is %s" % dbg.read_process_memory(args[1], args[2]))

	return DBG_CONTINUE


if __name__ == '__main__':
	for (pid, name)	in dbg.enumerate_process(): #  获取所有进程ID
		if name.lower() == processName:
			isProcess = True
			hooks = utils.hook_container()
			dbg.attach(pid) #  获取进程句柄
			print("process handle pid[%d]" % pid)
			hookAddress = dbg.func_resolve_debuggee("kernel32.dll", "WriteFile") #  获取断点API地址
			
			if hookAddress:
				hooks.add(dbg, hookAddress, 5, replaceString, None) #  注册钩子程序
				print("breakpoint is 0x%08x" % hookAddress)
				break
			else:
				print("can't resolve hook address")
				sys.exit(-1)

	if isProcess:
		dbg.run()
	else:
		print("no process [%s]" % processName )
		sys.exit(-1)
