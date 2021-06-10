# encoding: utf-8

from lxml import etree
import requests

def get_html():
    """
    下载网页到本地存储
    :return: 网页源代码
    """
    url = "https://uwintech.yuque.com/notifications/unread"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }
    response = requests.get(url, headers=headers).text
    with open("语雀.html", 'a', encoding='utf-8') as f:
        f.write(response)
        f.close()
    return response
    # print(response)
def xpath_html():
    tree = etree.parse('语雀.html', )
    x = tree.xpath('/html/head/meta')
    print(x)
    print(tree.xpath('/html//meta'))    # 表示层级
    print(tree.xpath('//meta'))         # 表示可以从任意位置查找meta标签
    print(tree.xpath('//meta[@name="description"]'))        # 表示所有的

if __name__ == '__main__':
    # get_html()
    xpath_html()
