# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 区名
    region = scrapy.Field()
    # 区域url
    regionUrls = scrapy.Field()

    # 二级url
    secondUrls = scrapy.Field()

    # 日期
    day = scrapy.Field()
    # 天气状况
    weatherConditions = scrapy.Field()
    # 气温
    temperature = scrapy.Field()
    # 风力风向
    windConditions = scrapy.Field()