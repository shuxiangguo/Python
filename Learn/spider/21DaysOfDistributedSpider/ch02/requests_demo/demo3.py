import requests

proxy = {
	'http': '39.137.2.194:8080'
}

response = requests.get("http://httpbin.org/ip", proxies=proxy)
print(response.text)