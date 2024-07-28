import random

import requests
import json


def get_sentence():
    url = 'https://v1.hitokoto.cn/'
    paras = {'c': random.choice('dehikl'), 'max_length': '20'}
    r = requests.post(url, params=paras)
    data = json.loads(r.text)
    return data['hitokoto'], data['from']


if __name__ == "__main__":
    print(get_sentence())
'''
a	动画
b	漫画
c	游戏
d	文学
e	原创
f	来自网络
g	其他
h	影视
i	诗词
j	网易云
k	哲学
l	抖机灵
'''
