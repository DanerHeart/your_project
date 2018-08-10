# -*- coding: utf-8 -*-
import scrapy
import urllib
from scrapy.http import Request,FormRequest
from simulate_login.items import SimulateLoginItem

class YourSpiderSpider(scrapy.Spider):
    name = 'your_spider'
    allowed_domains = ['douban.com']
#    start_urls=["https://www.douban.com/group/explore"]   
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"} #供登录模拟使用
    
    def start_requests(self):
        #url='https://www.douban.com/accounts/login'
        #return [Request(url=url,meta={"cookiejar":1},callback=self.parse)]#可以传递一个标示符来使用多个。如meta={'cookiejar': 1}这句，后面那个1就是标示符
        return [scrapy.FormRequest("https://accounts.douban.com/login", headers=self.headers, meta={"cookiejar":1}, callback=self.parse)]
    
    
    def parse_item(self,response):
        
        theitems=[]
        item = SimulateLoginItem()
        
        item['topic'] = response.xpath('//*[@id="content"]/h1/text()').extract()
        item['name']=response.xpath('//*[@id="content"]/div/div[1]/div[1]/div[2]/h3/span[1]/a/text()').extract()
        item['time']=response.xpath('//*[@id="content"]/div/div[1]/div[1]/div[2]/h3/span[2]/text()').extract()
        theitems.append(item)
        return theitems
        
    def parse_page(self,response):
#        href=response.xpath('//*[@id="db-nav-group"]/div/div/div[1]/a/text()').extract()
        href=response.xpath('//h3/a/@href').extract()
        for he in href:
            yield scrapy.Request(he,callback = self.parse_item)          
                 
             #爬取下一页
        unchange_url=['https://www.douban.com/group/explore']
        thenexthref = response.xpath('//div[@id="content"]/div/div[1]/div[2]/span[4]/a/@href').extract()
        real_url = [''.join(unchange_url+thenexthref)]
#        print(real_url)
#        print(type(real_url))         
        self.start_urls.append(real_url)
        if real_url:
            real_url=real_url[0]
            yield scrapy.Request(real_url,callback = self.parse_page)
        
        
    
    def log_in(self, response):
        #显示是否登录成功
        title = response.xpath('//title/text()').extract()[0]
        if u'登录豆瓣' in title:
            print("登录失败，请重试")
        else:
            print("登陆成功")
        yield scrapy.Request('https://www.douban.com/group/explore?start=30', callback = self.parse_page)  
        

    def parse(self, response):
        
        captcha = response.xpath('//*[@id="captcha_image"]/@src').extract()
        print(captcha)
        if len(captcha)>0:
            #有验证码，人工输入验证码
            urllib.request.urlretrieve(captcha[0],filename=r"C:\Users\LBX\your_project\simulate_login\simulate_login\captcha.png")
            captcha_value=input('查看captcha.png,有验证码请输入:')
            data={
                    "form_email":"18353113181@163.com",
                    "form_password":"9241113minda",
                    "captcha-solution":captcha_value,
                    }
        else:
            #此时没有验证码
            print("无验证码")
            data={
                    "form_email":"18353113181@163.com",
                    "form_password":"9241113minda",
                                        }
        print("正在登陆中.....")
        #进行登录
        return[
                FormRequest.from_response(
                        response,
                        meta={"cookiejar":response.meta["cookiejar"]},
                        headers=self.headers,
                        formdata=data,
                        callback=self.log_in,
                        )
                ]
        

            
        
