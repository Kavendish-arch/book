import scrapy

# scrapy genspider [name] 创建爬虫

class ThespiderSpider(scrapy.Spider):
    # scrapy crawl theSpider 运行爬虫
    name = 'theSpider'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com']

    def parse(self, response):
        print(response.xpath('./html/body/div[1]/div[2]/div[5]/div[1]/div/form/span[2]/input'))
        # print(response.text)

        pass
