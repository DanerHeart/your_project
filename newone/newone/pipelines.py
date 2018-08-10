# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import os

class NewonePipeline(object):
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        filename = base_dir + '/news.json'
        with codecs.open(filename, 'a') as f:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            f.write(line)
        return item

        
		 
		 
		
			
			
		

   
