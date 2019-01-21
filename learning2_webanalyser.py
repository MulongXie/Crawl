import re
from bs4 import BeautifulSoup as bs

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# initialize beautiful soup object
soup = bs(html_doc, 'html.parser')

# find/find_all(name('a'/'div'/'p'), attr(class_/href/style), string)
# attr supports regular expression

# attempt 1
# find all by tag name
links = soup.find_all('a')
print(type(links))
print(links)
for l in links:
    print(type(l), l['href'], l.get_text())
print('******\n')


# attempt 2
# find by tag name and class
links2 = soup.find_all('a', class_='sister')
for l in links2:
    print(l.name, l['href'], l.get_text())
print('******\n')


# attempt 3
# find by tag and regularity expression
link3 = soup.find('a', href=re.compile(r'll'))  # r support directly /, otherwise / = //
print(type(link3))  # if didn't find, the type of link/links would be nonetype
print(link3.name, link3['href'], link3.get_text())
print('******\n')


# attempt 4
# find the text in title paragraph
text = soup.find('p', class_='title')
print(type(text))
print(text)
print(text.name, text.get_text())
print('******\n')
