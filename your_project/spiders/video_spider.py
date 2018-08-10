# -*- coding: utf-8 -*-
import scrapy
from your_project.items import YourProjectItem 

class VideoSpiderSpider(scrapy.Spider):
    name = "video_spider"
    allowed_domains = ["v.qq.com"]
    start_urls = ['http://v.qq.com/x/list/tv?offset=0&iyear=2017&sort=4&iarea=-1']

    def parse(self, response):
        subselect = response.xpath('//div[@class="figure_title_score"]') # 嵌套匹配
        items = []
        for sub in subselect:
            item = YourProjectItem() # 结构化 item
            item['video_name'] = sub.xpath('./strong/a/text()').extract()[0] # 返回的是 list 所以 [0] 表示获取列表中的第一个元素，也就是字符串
            item['douban_score'] = sub.xpath('./div/em[@class="score_l"]/text()').extract()[0] + \
            sub.xpath('./div/em[@class="score_s"]/text()').extract()[0]
            items.append(item) # 存入 list
        return items
        #pass
