import time, requests, re


def link2(path2):
# 取出fiddler里json的文章标题和链接
    dic = dict()   # 创建字典记录标题和链接
    with open(path, "rb") as f:
        t = f.read().decode()
    json = re.search(r"general_msg_list\=([^\n]*)", t, re.S).group(1)  # 取出json内容
    json = eval(json)
    for msg in json["list"]:
        title = msg["app_msg_ext_info"]["title"]
        article = msg["app_msg_ext_info"]["content_url"]
        author = msg["app_msg_ext_info"]["author"]
        title = title + "_" + author
        if msg["app_msg_ext_info"]['multi_app_msg_item_list']:
            title1 = msg["app_msg_ext_info"]['multi_app_msg_item_list'][0]["title"]
            article1 = msg["app_msg_ext_info"]['multi_app_msg_item_list'][0]["content_url"]
            author1 = msg["app_msg_ext_info"]['multi_app_msg_item_list'][0]["author"]
            title1 = title1 + "_" + author1
            dic[title1] = article1
        dic[title] = article
    return(dic)


def link(path):
# 取出浏览器里的文章标题和链接
    dic=dict()  # 创建字典记录标题和链接
    with open(path, "rb") as f:
        t=f.read().decode()
    record=re.findall(r"<h4.*?</h4>", t, re.S)  # 取出h4标签内容
    for i in record:
       
        title_raw=re.search(r">(.*)</h4>", i, re.S).group(1)
        title=re.sub(r"<.*>|\s|\{.*\}", "", title_raw)
        if title:
            url_raw=re.search(r"http[^\"]*", i)
            if url_raw:
                url=url_raw.group()
                dic[title]=url
                # print("%s--%s" %(title,url))
                
        else:
            continue
    return(dic)


def main(path):
    # 创建txt记录公众号文章
    record = link(path)  # record=link2(path2)另一种方法备选
    # url="http://mp.weixin.qq.com/s?__biz=MzIwMzAwMzQxNw==&amp;mid=2756649160&amp;idx=1&amp;sn=a61d68641bd526e2e01fd288d1c9c890&amp;chksm=b76d83be801a0aa8c634992fa091ede37db94da9585e755cb893637b28b749d98b10ebe8997b&amp;scene=27#wechat_redirect"
    for key, value in record.items():

        art = article(key, value)
        with open("./%s.txt" %(key), "wb+") as f:
            f.write(art.encode())
            time.sleep(1)
    print("爬取完成")


def article(name, url):
    # 获取url对应的文章

    t = requests.get(url).text
    try:
        t = re.search(r"<div class=\"rich_media_content \".*?<script nonce=", t, re.S).group()  # 提取文章所在的标签段  
    except:
        print(Exception, name) 
        return(t)  
    else:             
        t = re.findall("(\"http.*?\")|(>.*?<)", t, re.S)  # 提取照片连接和文章('""', '><')
        art = str()  # 存储文章
        for (img,txt) in t:
            if img:
                art = art + re.search(r"\"(.*)\"", img, re.S).group(1)
            else:
                art = art + re.search(r">(.*)<", txt, re.S).group(1)
        return(re.sub(r"\&nbsp;", "\n",art))     


if __name__ == "__main__":
    path = "./pa.txt"  #获取浏览器里每篇文章的标题和链接
    path2 = "./fid.txt"  #通过fiddler获取web里的json会包含每篇文章的标题和链接
    main(path)  #main(path2)另一种方法备选
