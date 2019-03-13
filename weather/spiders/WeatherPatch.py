# -*- coding: utf-8 -*-
from random import randint
import re

import scrapy

from weather.items import WeatherItem


class LiaoningweatherSpider(scrapy.Spider):
    name = 'WeatherPatch'
    allowed_domains = ['www.tianqihoubao.com']

    regions = ['anshan', 'beipiao', 'benxi', 'benxixian', 'dashiqiao',
            'dandong', 'lnfengcheng', 'fushun', 'gaizhou', 'haicheng',
            'heishan', 'jianchang', 'jianping', 'kazuo', 'kaiyuan',
            'kuandian', 'panjin', 'panshan', 'qingyuan', 'suizhong',
            'taiping', 'xifeng', 'xingcheng', 'xiuyan', 'yingkou', 'zhangwu', 'zhuanghe']
    num_list = [[201101, 201207],
           [201712],
           [201109, 201505, 201712],
           [201101, 201102, 201103],
           [201212],
           [201102],
           [201102],
           [201808, 201812],
           [201708, 201709, 201712],
           [201609, 201806],
           [201509],
           [201712],
           [201101, 201102, 201711, 201712, 201901, 201902, 201903],
           [201101, 201102, 201103],
           [201209, 201307],
           [201809],
           [201701, 201702, 201703, 201704, 201705],
           [201411, 201412],
           [201710],
           [201806],
           [201101, 201102, 201311, 201312, 201801, 201802, 201803, 201804, 201806, 201807, 201808],
           [201211],
           [201710, 201402],
           [201412],
           [201806],
           [201402],
           [201102]]

    start_urls = []
    for i in range(len(regions)):
        region = regions[i]
        nums = num_list[i]
        for num in nums:
            url = 'http://www.tianqihoubao.com/lishi/{0}/month/{1}.html'.format(region, num)
            print('=====',url)
            start_urls.append(url)


    def parse(self, response):

        region = response.xpath('//h1/text()').extract()
        region = region[0].replace('\r\n','').replace(' ', '')
        print('region------',region)


        day = response.xpath('//table/tr[position()>1]/td[1]/a/text()').extract()
        weatherConditions = response.xpath('//table/tr[position()>1]/td[2]/text()').extract()
        temperature = response.xpath('//table/tr[position()>1]/td[3]/text()').extract()
        windConditions = response.xpath('//table/tr[position()>1]/td[4]/text()').extract()

        day = re.findall(r'\d+[\u4e00-\u9fa5_a-zA-Z0-9]+', str(day))

        for i in range(len(day)):
            item = WeatherItem()
            item['region'] = region[:4]
            item['day'] = day[i]
            item['weatherConditions'] = weatherConditions[i].replace('\r\n', '').replace(' ', '')
            item['temperature'] = temperature[i].replace('\r\n', '').replace(' ', '')
            item['windConditions'] = windConditions[i].replace('\r\n', '').replace(' ', '')
            yield item
