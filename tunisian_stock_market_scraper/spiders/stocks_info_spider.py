from pathlib import Path

import scrapy
import pandas as pd

class StockNamesSpider(scrapy.Spider):
    name = "stocks_info"

    def start_requests(self):
        urls = list(pd.read_csv('stocks_links.csv').link.values)[:0]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for ticker in response.css('.coth1::text').getall():
            yield {
                'name': ticker
            }