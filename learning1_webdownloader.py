import urllib.request as url
from http import cookiejar as cj

address = 'http://www.baidu.com'

# 1st method - classic
response = url.urlopen(address)
print(response.getcode())
cont = response.read()
print(len(cont))


# 2ed method - camouflage
request = url.Request(address)
request.add_header('user', 'Chrome')
response2 = url.urlopen(address)
print(response2.getcode())
print(len(response2.read()))


# 3rd method - additional capability
cookie = cj.CookieJar()
opener = url.build_opener(url.HTTPCookieProcessor(cookie))
url.install_opener(opener)   # now the urllib has the additional capability to process cookie
response3 = url.urlopen(address)
print(response3.getcode())
print(response3.read())
print(cookie)  # print the content of cookie
content = response3.read()


# add statement encoding='utf-8' as long as there is Chinese letter
file = open('output.html', 'w', encoding='utf-8')
file.write(content.decode('utf-8'))
file.close()