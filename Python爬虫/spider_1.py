import requests
import 
# 百度翻译爬取

url = "https://www.baidu.com/s"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
}
param = {
    "wd":'万门大学',
}


res = requests.get(url=url,params=param, headers=header)

# 爬取结果网页
# 结果编码转换
res.encoding = 'utf-8'
# 转存到html文件中
with open('wanmen.html','a') as add:
    add.write(res.text)

# 百度查词工具
def baidu_fanyi(word):
    url = 'https://fanyi.baidu.com/sug'
    data = {
    'kw': word
    }
    res = requests.post(url=url, data=data, headers=header)
    res.encoding = 'utf-8'
    return res.json()['data']

baidu_fanyi('message')

