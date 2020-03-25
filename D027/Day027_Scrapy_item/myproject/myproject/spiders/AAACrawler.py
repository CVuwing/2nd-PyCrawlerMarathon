# -*- coding: utf-8 -*-
import scrapy


class AaacrawlerSpider(scrapy.Spider):
    name = 'AAACrawler'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['http://www.ptt.cc/']

    def parse(self, response):
        pass
