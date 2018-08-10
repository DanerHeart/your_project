# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import codecs
import json

class YourProjectPipeline(object):
    def _init_(self):
        
        #self.file = codecs.open('items.json','wb',encoding='utf-8')
        
        with open("tencent-video.csv","a",newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["电视剧", "豆瓣评分"])
            
    def process_item(self, item, spider):
        
        #line = json.dumps(dict(item))+'\n'
        #self.file.write(line.decode("unicode_escape"))
        
        video_name = item['video_name']
        douban_score = item['douban_score']
        with open("tencent-video.csv","a",newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([video_name,douban_score])
        return item
