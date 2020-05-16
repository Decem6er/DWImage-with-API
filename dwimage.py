import requests
from PIL import Image
from io import BytesIO
import urllib
import urllib.request
import random

data = {"apikey":"xxx"}  #请求的参数
api = "192.168.0.101"
 
# 因为这里是读取图片，所以将解析json这步忽略掉
def get_date(data, api):
    data = urllib.parse.urlencode(data)
    url2 = api +'?'+ data
    response = requests.get(url2)
    me_json = response.json()
    return me_json  # 此处的返回值是元素为字典的列表
 
def getHtml(url):
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36'),('Referer',url)]
    urllib.request.install_opener(opener)
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def saveHtml(file_name, file_content):
    #    注意windows文件命名的禁用符，比如 /
    with open(file_name.replace('/', '_') + ".png", "wb") as f:
        #   写文件用bytes而不是str，所以要转码
        f.write(file_content)


response = get_date(data,api)
print(type(response))
print(response)
imgurl = response['data'][0]['url']
print(imgurl)

html = getHtml(imgurl)
saveHtml(str(random.randint(0,10)), html)
