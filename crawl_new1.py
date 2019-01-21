import html_downloader as hd
import html_parser as hp
from urllib.parse import quote
import urllib.request as ur
from bs4 import BeautifulSoup as bs
import re

url = 'https://baike.baidu.com/item/Python/407313'

res = ur.urlopen(url)

print(res.read())


