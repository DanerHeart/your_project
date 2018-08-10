# -*- coding: utf-8 -*-
import scrapy
from newone.items import NewoneItem

class MySpiderSpider(scrapy.Spider):
    name = "my_spider"
    allowed_domains = ["zhaopin.com"]
    start_urls = ["https://sou.zhaopin.com/jobs/searchresult.ashx?jl=538&kw=it&sm=0&p=1"]
    
    #得到URL。循环爬取
    def parse(self, response):
            href = response.xpath('//td[@class="zwmc"]/div/a[1]/@href').extract()
            for he in href:
                yield scrapy.Request(he,callback = self.parse_item)
                
            #爬取下一页
            thenexthref= response.xpath('//div[@class="newl'+'ist_wrap fl"]/div[@class="pages'+'Down"]/ul/li[@class="pagesDow'+'n-pos"]/a/@href').extract()
            
            self.start_urls.append(thenexthref)
            if thenexthref:
                thenexthref=thenexthref[0]
                yield scrapy.Request(thenexthref,callback=self.parse)
           
    
    #爬取具体的内容
    def parse_item(self,response):
        theitems =[]
        item = NewoneItem()
        a1 = response.xpath('//div[@class="terminalpage-left"]')
        temp1 = a1.xpath('./ul/li[1]/strong/text()').extract()[0]
        temp2 = ''
        for te in temp1:
            te = te.strip()
            if te!="":
                temp2 = temp2+te
        item['salary'] = temp2
        item['position'] = a1.xpath('./ul/li[2]/strong/a/text()').extract()
        item['time'] = a1.xpath('./ul/li[3]/strong/span/text()').extract()
        item['xingzhi'] = a1.xpath('./ul/li[4]/strong/text()').extract()
        item['experience'] = a1.xpath('./ul/li[5]/strong/text()').extract()
        item['education'] = a1.xpath('./ul/li[6]/strong/text()').extract()
        item['number'] = a1.xpath('./ul/li[7]/strong/text()').extract()
        item['leibie'] = a1.xpath('./ul/li[8]/strong/a/text()').extract()
        theitems.append(item)
        
        return theitems

        