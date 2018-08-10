# -*- coding: utf-8 -*-
import scrapy


class YouSpiderSpider(scrapy.Spider):
    name = 'you_spider'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']

    def parse(self, response):
        pass
