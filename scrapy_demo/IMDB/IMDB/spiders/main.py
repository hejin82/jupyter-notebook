import scrapy
from scrapy.http import Response

class ScratchImdb(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/top']

    def parse(self, response):
        for i in response.css('ul.ipc-metadata-list'):
            url = i.css('a.ipc-title-link-wrapper').css('::attr(href)').get()
            self.logger.info("url:%s", url)
            yield response.follow(url, callback=self.parse_info)

    def parse_info(self, response):
        self.logger.info("received for %s", response.url)