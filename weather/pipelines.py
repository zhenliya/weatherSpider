# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class WeatherPipeline(object):
    # item是对应的数据，spider是爬虫
    def __init__(self):
        self.file = open('weather.json','a',encoding='utf-8')

    def process_item(self, item, spider):
        # city = item['city']
        # region = item['region']
        # day = item['day']
        # weatherConditions = item['weatherConditions']
        # temperature = item['temperature']
        # windConditions = item['windConditions']
        line = json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()

class WeatherPatchPipeline(object):
    # item是对应的数据，spider是爬虫
    def __init__(self):
        self.file = open('weatherPatch.json','a',encoding='utf-8')

    def process_item(self, item, spider):
        # city = item['city']
        # region = item['region']
        # day = item['day']
        # weatherConditions = item['weatherConditions']
        # temperature = item['temperature']
        # windConditions = item['windConditions']
        line = json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()

class WeatherPatchPipeline2(object):
    # item是对应的数据，spider是爬虫
    def __init__(self):
        self.file = open('kazuo2.json','a',encoding='utf-8')

    def process_item(self, item, spider):
        # city = item['city']
        # region = item['region']
        # day = item['day']
        # weatherConditions = item['weatherConditions']
        # temperature = item['temperature']
        # windConditions = item['windConditions']
        line = json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()