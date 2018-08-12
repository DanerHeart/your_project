# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from crawl_movie.items import CrawlMovieItem
import re
from urllib import parse

class MovieSpiderSpider(scrapy.Spider):
    name = 'movie_spider'
    allowed_domains = ['dytt8.net']
    start_urls = ['http://www.dytt8.net/html/gndy/dyzz/index.html']
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"} #供登录模拟使用
    
    def parse(self, response):
        
        theitem =[] 
        item = CrawlMovieItem()
        
        start_url = "http://www.dytt8.net/html/gndy/dyzz/20180718/57146.html"      #用于构建完整的url
#        print("is parse :%s"%response.url)
        rep = re.compile("<.*?>")                #用于提取电影内容的正则表达式
        mat = r".*/\d+/\d+\.html"                #用于匹配需要爬取网页的正则表达式
        urls = response.xpath("//a/@href").extract()    #scrapy的选择器语法,用于提取网页链接
        data = response.body            #响应的文本
        soup = BeautifulSoup(data,"lxml")       #构建BeautifulSoup对象
        content = soup.find("div",id="Zoom")       #电影信息元素
        if content:
            sources = content.find_all("a")         #电影下载地址元素
            source = []             #电影下载地址
            if sources:
                for link in sources:
                    source.append(link.text)
                if source:
                    print('')
                else:
                    print('0000000000000000000000000000000000000000000000000000000000000')
                    
                    
                if "ftp" in source[0]:
                    item['download_link'] = source[0]
                else:
                    item['download_link'] = source[1]
                           
            names = soup.find("title")       #电影名称
            if names:
                names = names.text
                item['movie_name']=names
#            print(item)
            theitem.append(item)           
            yield item      #返回数据类
        
        for url in urls:
                if re.match(mat,url) != None:
                    full_url = parse.urljoin(start_url,url)      #返回进一步爬取的url
                    yield scrapy.Request(url=full_url,callback=self.parse)


