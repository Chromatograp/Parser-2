# -*- coding: utf-8 -*-
import scrapy


class ScraperSpider(scrapy.Spider):
    name = 'scraper'
    allowed_domains = ['first-buggy.ru/catalog/%D0%94%D0%B5%D1%82%D1%81%D0%BA%D0%B8%D0%B5-%D0%BA%D0%BE%D0%BB%D1%8F%D1%81%D0%BA%D0%B8/']
    start_urls = ['http://first-buggy.ru/catalog/%D0%94%D0%B5%D1%82%D1%81%D0%BA%D0%B8%D0%B5-%D0%BA%D0%BE%D0%BB%D1%8F%D1%81%D0%BA%D0%B8//']

    def parse(self, response):
        pass
