fname = "hello.bmp"
#  读取图片
pfile = open(fname, "r+b")
buff = pfile.read()
buff.replace(b'\x2A\x2F', b'\x00\x00') #  去除*/
pfile.close()
#  图片插入注释
pfile = open(fname, "w+b")
pfile.write(buff)
pfile.seek(2, 0) #  起始位置偏移2字节BM
pfile.write(b'\x2F\x2A') #  BM后加*/注释
pfile.close()
#  图片插入脚本
pfile = open(fname, "a+b")
pfile.write(b'\xFF\x2A\x2F\x3D\x31\x3B') #  注释*/=1;
pfile.write(open('hello.js', "rb").read()) #  追加js脚本
pfile.close()
