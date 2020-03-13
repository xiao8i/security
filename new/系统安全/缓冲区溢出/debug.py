from pydbg import *
from pydbg.defines import *
import struct, utils


#  fuzzing测试调试
processname = "xxx.exe"
dbg = pydbg()
def handler(dbg):
	#  回调函数：用来保存事件发生时的内存状态
	crash = utils.crash_binning.crash_binning()
	crash.record_crash(dbg)
	print(crash.crash_synopsis())
	dbg.terminate_process()


for (pid, name) in dbg.enumerate_process():
	if name == processname:
		print("dbg:" + name)
		dbg.attach(pid)
dbg.set_callback(EXCEPTION_ACCESS_VIOLATION, handler) #  设置事件发生时的回调函数
dbg.run()