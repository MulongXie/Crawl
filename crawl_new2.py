import re
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

root = 'http://baike.baidu.com'

file = open('output.txt', 'r', encoding='utf-8')
content = file.read()

soup = bs(content, 'html.parser')

link = soup.find_all('a')
for l in link:
    try:
        ll = l['href']
        fl = urljoin(root, ll)
        print(fl)
    except:
        # print(l)
        continue
