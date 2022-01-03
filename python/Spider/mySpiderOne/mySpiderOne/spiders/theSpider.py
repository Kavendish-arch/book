import scrapy


class ThespiderSpider(scrapy.Spider):
    name = 'theSpider'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
