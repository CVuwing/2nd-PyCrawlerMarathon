# -*- coding: utf-8 -*-
import scrapy


class PttcrawlerSpider(scrapy.Spider):
    name = 'PTTCrawler'
    allowed_domains = ['www.ptt.cc/bbs/Stock/M.1585019593.A.08A.html']
    start_urls = ['https://www.ptt.cc/bbs/Stock/M.1585019593.A.08A.html/']

    def parse(self, response):
        pass
