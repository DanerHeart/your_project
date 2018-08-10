# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem

class WuhanspiderSpider(scrapy.Spider):
    name = 'wuhanSpider'
    allowed_domains = ['wuhan.tianqi.com']
    citys = ['wuhan','shanghai']
    start_urls = ['https://www.tianqi.com/wuhan/']
    


    def parse(self, response):
        subSelector = response.xpath('//div[@class="wrap1100"]')
        #response.xpath('//div[@class="wrap1100"]/div[2]/div[2]/ul/li/b/text()')').extract()
        items =[]
        item = WeatherItem()
        item['cityDate'] = subSelector.xpath('./div[2]/div[2]/ul/li/b/text()').extract()
        item['week'] = subSelector.xpath('./div[2]/div[2]/ul/li/span/text()').extract()
        items.append(item)
        return items
        #pass
