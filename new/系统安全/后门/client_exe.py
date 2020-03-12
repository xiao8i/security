import py2exe
from distutils.core import setup


"""后门客户端exe文件"""
options = {"bundle_files" : 1, "compressed" : 1, "optimize" : 2} #  包括python解释器一起打包，压缩，额外优化
setup = (console = ["client.py"], options = {"py2exe" : options}, zipfile = None) #  指定client.py
# 执行python -u client_exe.py py2exe,exe文件在dist目录
