from urllib import parse

url = "http://www.baidu.com/s;hello?wd=python&password=123#a"

# urlparse和urlsplit的区别在于params   url里;he ?之间的内容
result = parse.urlparse(url)
result2 = parse.urlsplit(url)
print(result)
print(result2)
print("netloc", result.netloc)