# 安装并使用 requests、bs4 库，爬取猫眼电影（）的前 10 个
# 电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
import requests
from bs4 import BeautifulSoup as bs

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
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
        my_type = t_info[1].find('span', ).nextSibling.replace(" ", "").replace('\n', '')
        # 日期
        my_date = t_info[3].find('span', ).nextSibling.replace(" ", "").replace('\n', '')
        tmp = [my_name, my_type, my_date]
        m_list.append(tmp)
    return m_list;


my_list = get_url_name('https://maoyan.com/films?showType=3')
import pandas as pd

my_data = pd.DataFrame(my_list)
my_data.to_csv('./maoyan.csv', encoding='utf8', index=False, header=False)
