#  缓冲区数据样例


junk = "\x41" * 260 #  A*260，,260个数需要fuzzing测试
junk += "jmp esp" #  这里原本保存RETN时传递给EIP的地址，我们改为jmp esp指令的内存地址,这样RETN时就可以执行jmp esp的命令，注意高位在后
junk += "\x90" * 16 #  多个NOPS指令，提供滑动
junk += "shellcode" #  shellcode在栈中，并通过5中jmp esp指令指向栈来运行