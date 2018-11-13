from urllib import request
from urllib import parse

# urlretrive函数的用法
# url = "http://pic10.nipic.com/20101020/6007208_215114083000_2.jpg"
# res = request.urlretrieve(url, 'dog.jpg')

# urlencode函数的用法
# params = {'name': "张三", "age": 18, 'greet': "hello world"}
# result = parse.urlencode(params)
# print(result)


# url = "https://www.baidu.com/s"
# params = {"wd": "刘德华"}
# qs = parse.urlencode(params)
# url = url + "?" + qs
# resp= request.urlopen(url)
# print(resp.read())


# parse_qs函数的用法
params = {"name": '张三', "age": 18, "greet": "hello world"}
qs = parse.urlencode(params)
print(qs)

res = parse.parse_qs(qs)
print(res)
print(res['name'])