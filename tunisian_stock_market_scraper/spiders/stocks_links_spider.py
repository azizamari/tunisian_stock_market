from pathlib import Path

import scrapy


class StocksLinksSpider(scrapy.Spider):
    name = "stocks_links"

    def start_requests(self):
        urls = [
            'https://www.ilboursa.com/marches/aaz',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for link in response.css('.allf a::attr(href)').getall():
            name=link[9:]
            yield {
                'name':name,
                'link':'https://www.ilboursa.com/marches/'+link
            }