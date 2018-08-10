# -*- coding: utf-8 -*-
import time
import os.path
import urllib2
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WeatherPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d', time.localtime())
        fileName = today+'txt'
        with open(fileName,'a') as fp:
            fp.write(item['cityDate'].encode('utf8')+'\t')
            fp.write(item['week'].encode('utf8')+'\t')
        return item
