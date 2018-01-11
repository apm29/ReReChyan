# -*- coding:utf-8 -*-

import os
import json
import urllib.request

import requests


def func():
    print('function')


def func2(num1, str1):
    str1.to_bytes(1, byteorder='big')
    print(type(str1))
    print(str(num1), str1)


name = 'ReRe#niji1997'
icon = 'bakyura-2x'
file_name = 'ReRe.cookie'
# url_room = input('Input the [Room URL] ')
url_room = "http://drrr.com/room/?id=ospL3a5aVf"

fileConfig = open('config.txt', mode='rb+')

print(fileConfig.mode)
# for line in fileConfig.readlines():
#     # print(line)
#     print(line.decode(encoding='utf-8'))

for line in fileConfig.read(3):
    print(line)
path = "newDir"
if path:
    try:
        if not os.path.exists(path):
            os.makedirs(path)
        os.chdir(path)
        f = open('b.txt', 'a')
        print(f.tell())
        f.write('123 = 123\n')
    except Exception as e:
        print('error:', e)
num = 3
print('python %d' % num)
print(bool(None))
func()
func2(1, 2)

rng = range(1, 10, 2)
print(type(rng))
lst = (1, 2, 3, 4)
print(type(lst))
lst = [1, 2, 3, 4]
print(type(lst))
lst = {1, 2, 3, 4}
print(type(lst))
for i in rng:
    print(i)

url = "http://www.weather.com.cn/data/cityinfo/101010100.html"
fp = urllib.request.urlopen(url)
print(type(fp))
myBytes = fp.read()
myStr = myBytes.decode("utf8")
fp.close()
bean = json.loads(myStr)
weather = bean['weatherinfo']
city = weather['city']
print(city)

resp = requests.get(url)
print(resp.content.decode('utf-8'))
print(type(resp.content))
i = 1
sum_ = 0
while i < 10000:
    c = 7 * (2 * i - 1)
    m = 8 ** i
    sum_ += c / m
    i += 1
print("计算10000项 = %.20f" % sum_)
a = 7 / 8 + 21 / 64 + 35 / 512
print(' 7/8 + 21/64 + 35/512 = %.20f' % a)
print('51/49 = %.20f' % (51 / 49))
print('63/49 = %.20f' % (63 / 49))
