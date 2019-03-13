# -*- coding: utf-8 -*-
from random import randint
import re

import scrapy
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider
# from scrapy.spiders import Rule
from weather.items import WeatherItem


class LiaoningweatherSpider(scrapy.Spider):
    name = 'LiaoNingWeather'
    allowed_domains = ['www.tianqihoubao.com']
    start_urls = ['http://www.tianqihoubao.com/lishi/ln.htm']

    # rules = [
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # ]

    def parse(self, response):
        items = []

        region = response.xpath('//div[@class="citychk"]/dl/dd/a/text()').extract()
        regionUrls = response.xpath('//div[@class="citychk"]/dl/dd/a/@href').extract()

        for j in range(len(region)):
            item = WeatherItem()
            item['region'] = region[j]
            item['regionUrls'] = 'http://www.tianqihoubao.com' + regionUrls[j]
            items.append(item)

        for item in items:
            num = randint(1,10)
            headers = {
                "Host": " www.tianqihoubao.com",
                "Connection": " keep-alive",
                "Upgrade-Insecure-Requests": " 1",
                "User-Agent": " Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Referer": item['regionUrls'],
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Cookie": " bdshare_firstime=1551774929120; ASP.NET_SessionId=aqw2rlecjphgfgauhkd1jt55; Hm_lvt_f48cedd6a69101030e93d4ef60f48fd0=1551774929,1551832490; __51cke__=; __tins__4560568=%7B%22sid%22%3A%201551832491486%2C%20%22vd%22%3A%2011%2C%20%22expires%22%3A%201551836030491%7D; __51laig__={};Hm_lpvt_f48cedd6a69101030e93d4ef60f48fd0=1551834231".format(num)
            }
            yield scrapy.Request(url=item['regionUrls'], meta={'meta_1': item}, callback=self.second_parse,
                                 headers=headers)

    def second_parse(self, response):
        meta_1 = response.meta['meta_1']
        secondUrls = response.xpath('//div[@id="content"]/div/ul/li/a/@href').extract()
        items = []
        # for i in range(len(secondUrls)):
        for i in range(3):
            # if_belong = secondUrls[i].startswith[meta_1['regionUrls'][28:-5]] or secondUrls[i].startswith[
            #     meta_1['regionUrls'][35:-5]]
            # print('----if_belong:',if_belong)
            # if if_belong:
            item = WeatherItem()
            item['region'] = meta_1['region']
            item['regionUrls'] = meta_1['regionUrls']
            if secondUrls[i].startswith('/lishi'):
                item['secondUrls'] = 'http://www.tianqihoubao.com' + secondUrls[i]
            else:
                item['secondUrls'] = 'http://www.tianqihoubao.com/lishi/' + secondUrls[i]
            items.append(item)
        for item in items:
            num = randint(11, 20)
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8 ",
                "Referer": item['secondUrls'],
                "Host": " www.tianqihoubao.com ",
                "Connection: keep-alive Upgrade-Insecure-Requests": " 1 ",
                "User-Agent": " Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36 ",
                "Accept-Encoding": " gzip, deflate ",
                "Accept-Language": " zh-CN,zh;q=0.9 ",
                "Cookie": " bdshare_firstime=1551774929120; ASP.NET_SessionId=aqw2rlecjphgfgauhkd1jt55; Hm_lvt_f48cedd6a69101030e93d4ef60f48fd0=1551774929,1551832490; __51cke__=; Hm_lpvt_f48cedd6a69101030e93d4ef60f48fd0=1551834530; __tins__4560568=%7B%22sid%22%3A%201551834440385%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201551836330045%7D; __51laig__={}".format(num)
            }

            yield scrapy.Request(url=item['secondUrls'], meta={'meta_2': item}, callback=self.detail_parse,
                                 headers=headers)

    def detail_parse(self, response):

        meta_2 = response.meta['meta_2']
        day = response.xpath('//table/tr[position()>1]/td[1]/a/text()').extract()
        weatherConditions = response.xpath('//table/tr[position()>1]/td[2]/text()').extract()
        temperature = response.xpath('//table/tr[position()>1]/td[3]/text()').extract()
        windConditions = response.xpath('//table/tr[position()>1]/td[4]/text()').extract()

        day = re.findall(r'\d+[\u4e00-\u9fa5_a-zA-Z0-9]+', str(day))

        for i in range(len(day)):
        # for i in range(3):
            item = WeatherItem()
            item['region'] = meta_2['region']
            item['day'] = day[i]
            item['weatherConditions'] = weatherConditions[i].replace('\r\n','').replace(' ','')
            item['temperature'] = temperature[i].replace('\r\n','').replace(' ','')
            item['windConditions'] = windConditions[i].replace('\r\n','').replace(' ','')
            yield item
