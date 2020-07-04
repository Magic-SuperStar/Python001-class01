# 安装并使用 requests、bs4 库，爬取猫眼电影（）的前 10 个
# 电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
import lxml
import requests
from bs4 import BeautifulSoup as bs

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {'user-agent': user_agent}


def get_url_name(url):
    response = requests.get(url, headers=header)
    my_info = bs(response.text, 'html.parser')
    m_list = []
    for tags in my_info.find_all('div', attrs={'class': 'movie-hover-info'})[:10]:
        t_info = tags.find_all('div', attrs={'class': 'movie-hover-title'})
        # 名字
        my_name = t_info[0].find('span', ).text
        # 类型
        my_type = t_info[1].find('span', ).nextSibling.strip()
        # 日期
        my_date = t_info[3].find('span', ).nextSibling.strip()
        tmp = [my_name, my_type, my_date]
        m_list.append(tmp)
    return m_list;


###### 第二种方法


def get_info(t_url):
    response = requests.get(t_url, headers=header)
    # xml化处理
    selector = lxml.etree.HTML(response.text)
    # 名字
    my_name = selector.xpath('//div[@class="movie-brief-container"]/h1/text()')
    # 类型
    my_type = selector.xpath('//div[@class="movie-brief-container"]/ul/li[1]/a/text()')
    # 日期
    my_date = selector.xpath('//div[@class="movie-brief-container"]/ul/li[3]/text()')
    return [my_name[0], ','.join(my_type), my_date[0]]


m_url = 'https://maoyan.com'


def get_urls(url):
    response = requests.get(url, headers=header)
    i_url = bs(response.text, 'html.parser')
    m_list = []
    for tags in i_url.find_all('div', attrs={'class': 'movie-item film-channel'})[:10]:
        t_url = tags.find('a', ).get('href')
        m_list.append(get_info(m_url + t_url))
    return m_list


import pandas as pd

my_list = get_urls('https://maoyan.com/films?showType=3')

my_data = pd.DataFrame(data=my_list)
my_data.to_csv('./maoyan01.csv', encoding='utf-8', index=False, header=False)
