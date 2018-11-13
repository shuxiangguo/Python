from urllib import request
# 不使用cookie
url = 'http://www.renren.com/880151247/profile'
headers = {
	'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
	'Cookie': 'anonymid=jnrg8h32-fj7qey; depovince=AH; _r01_=1; ick_login=de7d3a0a-d5fd-4ebe-8f68-18ba4fd86bfa; t=b6e77634c431fb5387a678f07634c7722; societyguester=b6e77634c431fb5387a678f07634c7722; id=968496142; xnsid=4a6686c1; jebecookies=65498b63-35ef-4000-b0ef-9fbc2e07522d|||||; ver=7.0; loginfrom=null; jebe_key=c4feca0e-a3e0-4956-a6b7-05bdee9fa1d6%7Cf09f1091a15b74910c76d0fb3537dd14%7C1540645031862%7C1%7C1540645034549; wp_fold=0'
}

req = request.Request(url=url, headers=headers)
resp = request.urlopen(req)
with open('renren.html', 'w', encoding='utf-8') as fp:
	# write函数必须写入一个str的数据类型
	# resp.read函数读出来的是一个bytes数据类型
	# bytes -> decode() -> str
	# str -> encode() -> bytes
	fp.write(resp.read().decode('utf-8'))
