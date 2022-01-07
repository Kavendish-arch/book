import sqlite3
from bs4 import BeautifulSoup
import time
import requests

img_link = ""
pic_title = 'imgs/%s.jpg'%img_link.split('/')[2].split('.')[0]


def download_picture(img_link, pic_title):
    """
        功能：下载图片
        参数 图片网址，图片保存路径
    """
    img = requests.get(img_link).content
    with open(pic_title, 'wb') as f:
        f.write(img)
