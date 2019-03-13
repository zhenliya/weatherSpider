# -*- coding: utf-8 -*-
from random import randint
import re

import scrapy

from weather.items import WeatherItem


class LiaoningweatherSpider(scrapy.Spider):
    name = 'WeatherPatch2'
    allowed_domains = ['www.tianqihoubao.com']

    # regions = ['jianping', 'panshan',
    #         'taiping']
    # num_list = [[2018],
    #             [2015,2016,2017],
    #             [2014,2015,2016,2017]]
    # num2 = ['01','02','03','04','05','06','07','08','09','10','11','12']
    #
    # start_urls = []
    # for i in range(len(regions)):
    #     region = regions[i]
    #     nums = num_list[i]
    #     for num in nums:
    #         for n in num2:
    #             url = 'http://www.tianqihoubao.com/lishi/{0}/month/{1}{2}.html'.format(region, num, n)
    #             print('=====',url)
    #             start_urls.append(url)
    start_urls =['http://www.tianqihoubao.com/lishi/kazuo/month/201608.html']


    def parse(self, response):

        region = response.xpath('//h1/text()').extract()
        region = region[0].replace('\r\n','').replace(' ', '')
        print('region------',region)
        print(response)


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
