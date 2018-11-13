# urllib request.Request学习

from urllib import request
from urllib import parse

url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="

# resp = request.urlopen(url)
# print(resp.read())

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
			"Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
		   }
# req = request.Request(url, headers=headers)
# resp = request.urlopen(req)
# print(resp.read())


data = {
	'first': True,
	'pn': 1,
	'kd': 'python'
}

req = request.Request(url, headers=headers, data=parse.urlencode(data).encode('utf-8'), method='POST')
resp = request.urlopen(req)

index = open('index.html', 'w', encoding='utf-8')
# index.write(resp.read().decode('utf-8'))
print(resp.read().decode('utf-8'), file=index)

