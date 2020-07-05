import scrapy
from scrapy.selector import Selector

from maoyan.items import MaoyanItem


class SmaoyanSpider(scrapy.Spider):
    name = 'smaoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/films']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)

    m_url = 'https://maoyan.com'

    def parse(self, response):
        # urls = [self.m_url + movie.extract_first() for movie in
        #         Selector(response).xpath('//div[@class="movie-item film-channel"]/a/@href')[:10]]
        movies = Selector(response).xpath('//div[@class="movie-item film-channel"]')[:10]
        for movie in movies:
            t_url = self.m_url + movie.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=t_url, callback=self.getInfo)

    def getInfo(self, response):
        m_movies = Selector(response).xpath('//div[@class="movie-brief-container"]')
        for info in m_movies:
            item = MaoyanItem()
            item['film_name'] = info.xpath('./h1/text()').extract_first()
            film_types = info.xpath('./ul/li[1]/a/text()').extract()
            item['film_type'] = (','.join(film_types)).strip()
            item['plan_date'] = info.xpath('./ul/li[3]/text()').extract_first()
            yield item