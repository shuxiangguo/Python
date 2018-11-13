from urllib import request
from http.cookiejar import CookieJar
from urllib import parse


headers = {
		'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
	}


def get_opener():

	# 1. 登录
	# 1.1 创建一个cookiejar对象
	cookiejar = CookieJar()

	# 1.2 使用cookiejar创建一个HTTPCookieProcessor对象
	handler = request.HTTPCookieProcessor(cookiejar)

	# 1.3 使用上一步常见的handler创建一个opener
	opener = request.build_opener(handler)
	return opener


def login_ren_ren(opener):

	# 1.4 使用opener发送登录的请求（人人网的邮箱和密码）
	data = {
		'email': "9701380749@qq.com",
		'password': "pythonspider"
	}

	login_url = 'http://www.renren.com/PLogin.do'

	### 经测试type(urlencode(data)) == str
	req = request.Request(login_url, data=parse.urlencode(data).encode('utf-8'), headers=headers)
	opener.open(req)


def visit_profile(opener):
	# 2. 访问个人主页
	dapen_url = 'http://www.renren.com/880151247/profile'
	req = request.Request(dapen_url, headers=headers)
	resp = opener.open(req)
	with open('renren.html', 'w', encoding='utf-8') as fp:
		fp.write(resp.read().decode('utf-8'))


if __name__ == '__main__':
	opener = get_opener()
	login_ren_ren(opener)
	visit_profile(opener)