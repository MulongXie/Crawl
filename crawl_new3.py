import urllib.request as ur
from urllib.parse import quote
from bs4 import BeautifulSoup as bs
import string

url = 'https://baike.baidu.com/item/秒懂全视界'

response = ur.urlopen(quote(url, safe=string.printable))
content = response.read()
soup = bs(content, 'html.parser')
links = soup.find_all('a')

title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
t = title.get_text()
print(t)
print(type(t))

file = open('output.txt', 'w', encoding='utf-8')
file.write(t)
file.close()