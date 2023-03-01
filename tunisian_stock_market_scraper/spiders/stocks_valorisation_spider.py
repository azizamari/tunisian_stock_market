from pathlib import Path

import scrapy
import pandas as pd

class StockValoSpider(scrapy.Spider):
    name = "stocks_valo"
    def start_requests(self): 
        url_list=list(pd.read_csv('stocks_links.csv').link.values)
        for url in url_list:                                              
            yield scrapy.Request(url = url, callback = self.parse)          

    def parse(self, response):
        ch=response.css('.coth1::text').getall()[0]
        value=str(response.css('.cot_v22 > div::text').getall()[-1])
        value=value.replace('"','')
        yield {
            'Ticker':ch[ch.index('Ticker')+9:],
            'Market Cap': value
        }