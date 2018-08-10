# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YourProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    video_name = scrapy.Field()
    douban_score = scrapy.Field()
    #pass
