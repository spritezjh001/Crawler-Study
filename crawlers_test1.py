import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')
print(response.code)
print(response.read())



