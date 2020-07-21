import time

import scrapy
from scrapy.selector import Selector
from hw01_mysql.items import Hw01MysqlItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    url = 'https://maoyan.com/films?showType=3&offset='
    offset = 1
    start_urls = [url + str(offset)]

    def start_requests(self):
        page = 1
        for offset in range(2):
            page += 1
            url = self.url + str(offset * 30)
            yield scrapy.Request(url, callback=self.parse,
                                 meta={'offset': offset * 30, 'page': page},
                                 dont_filter=True)

    h_url = 'https://maoyan'

    # 找到top250条数据
    def parse(self, response):
        for m in Selector(response).xpath('//div[@class="movie-item film-channel"]'):
            url = self.h_url + m.xpath('./a/@href').extract_first()
            # time.sleep(10)
            yield scrapy.Request(url, callback=self.getInfo)

    def getInfo(self, response):
        movie = Selector(response).xpath('//div[@class="movie-brief-container"]')
        item = Hw01MysqlItem()
        item['connect_url'] = response.url
        item['film_name'] = movie.xpath('./h1/text()').extract_first()
        ftypes = movie.xpath('./ul/li[1]/a/text()').extract()
        item['film_type'] = (','.join(ftypes)).strip()
        item['plan_date'] = movie.xpath('./ul/li[3]/text()').extract_first()
        yield item
