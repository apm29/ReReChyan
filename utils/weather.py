import re
import urllib.request
from utils import city as city_codes
import json

# 之所以能知道一个城市的天气，是因为用了中国天气网（www.weather.com.cn）提供的天气查询接口。在浏览器里试着访问一下：
# http://www.weather.com.cn/data/cityinfo/101010100.html
#
# 你就能看到北京现在的天气。这段看上去有点像python中字典类的文字是一种称作json格式的数据。
#
#
#
# 而我们的程序要做的事情，就是按照用户输入的城市名称，去天气网的接口请求对应的天气信息，再把结果展示给用户。
#
#
#
# 于是，在这个程序中，我们要用到两个新模块：
#
# 1. urllib2
#
# 用来发送网络请求，获取数据
#
#
#
# 2. json
#
# 用来解析获得的数据
#
#
#
# 听上去似乎还挺不算太复杂？但是注意刚才那个例子，我们请求北京天气时，用了“101010100”这样的数字。这是天气网设定的城市代码。然而令人蛋疼的是，天气网并没有直接给出所有城市代码的对应关系，而是给了3个接口：
#
#
#
# 1. http://m.weather.com.cn/data3/city.xml
#
# 获取所有省/直辖市的编号，如“01|北京,02|上海,03|天津”
#
#
#
# 2. http://m.weather.com.cn/data3/city省编号.xml
#
# 获取二级地区编号，如江苏是：city19.xml
#
#
#
# 3. http://m.weather.com.cn/data3/city二级编号.xml
#
# 获取三级编号，如南京是：city1901.xml
#
#
#
# 得到最终的三级编号之后，再加上中国101的前缀，就得到了城市代码，如南京市区就是“101190101”
#
#
#
# 所以，你可以选择，再写一个python程序，事先把这些复杂的编码全部抓取下来，整理成你要的格式；或者，偷懒一下，跳过这个过程，直接拿我抓好的编码。我放在了网盘里：
#
# https://pan.baidu.com/s/1c0Nw4m
url_query_city = 'http://www.weather.com.cn/data/cityinfo/{0}.html'


def get_city_url_by_code(city):
    return url_query_city.format(city)


def get_city_url(city):
    code = city_codes.city.get(city)
    return get_city_url_by_code(code)


def get_city_weather(city='诸暨'):
    try:
        url = get_city_url('%s' % city)

        print(url)
        resp = urllib.request.urlopen(url)
        return CityWeather(resp.read().decode('utf-8'))
    except Exception as e:
        print('查询失败: ' + str(e))
        return None


class CityWeather:
    def __init__(self, str_json):
        bean = json.loads(str_json)
        weather_bean = bean['weatherinfo']
        self.city = weather_bean['city']
        self.city_id = weather_bean['cityid']
        self.temp1 = weather_bean['temp1']
        self.temp2 = weather_bean['temp2']
        self.weather = weather_bean['weather']
        self.img1 = weather_bean['img1']
        self.img2 = weather_bean['img2']
        self.p_time = weather_bean['ptime']


weather = get_city_weather('诸暨')
if weather:
    print(weather.weather)
else:
    print('查询失败')

# 从下面一段文本中，匹配出所有s开头，e结尾的单词。
s1 = 'site sea sue sweet see case sse ssee loses'
lists = re.findall(r'\bs\S*e\b', s1)
for i in lists:
    print(i)
s2 = '18628145340'
print(re.match(r'1\d{9}', s2))