from pathlib import Path

import scrapy


class StockNamesSpider(scrapy.Spider):
    name = "stock_names"

    def start_requests(self):
        urls = [
            'https://www.ilboursa.com/marches/aaz',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for stock in response.css('.allf a::text').getall():
            yield {
                'name': stock
            }

