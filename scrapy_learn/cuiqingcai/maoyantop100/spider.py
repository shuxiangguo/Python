import json
import re
import requests

from multiprocessing import Pool
from requests.exceptions import RequestException

def get_one_page(url):
    try:
        res = requests.get(url)
        print(res.status_code)
        if res.status_code == 200:
            return res.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile("<dd>", re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            "index": item[0],
            "image": item[1],
            "title": item[2],
            "actor": item[3].strip()[3:],
            "time": item[4].strip()[5:],
            "score": item[5]
        }

def write_to_file(content):
    with open("result.txt", "a", encoding="utf-8") as f:
        # content是一个字典的形式，需要使用json.dump转换成字符串形式
        f.write(json.dump(content, ensure_ascii=False) + '\n')
        f.close()

def main(offset):
    url = "https://maoyan.com/board/4?" + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == "__main__":
    pool = Pool()
    pool.map(main, [i*10 for i in range(10)])