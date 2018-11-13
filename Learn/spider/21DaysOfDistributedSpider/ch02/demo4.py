from urllib import request

# # 没有使用代理
# url = "http://httpbin.org/ip"
# resp = request.urlopen(url)
# print(resp.read())

# 使用代理
# proxyHandler
url = "http://httpbin.org/ip"
proxyHandler = request.ProxyHandler({"http": "39.137.2.194:8080"})
opener = request.build_opener(proxyHandler)

resp = opener.open(url)
print(resp.read())