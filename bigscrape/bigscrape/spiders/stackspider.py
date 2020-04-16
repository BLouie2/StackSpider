# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy import Spider
from scrapy.selector import Selector
from bigscrape.items import BigscrapeItem


class StackspiderSpider(Spider):
    name = 'stackspider'
    allowed_domains = ['stackoverflow.com']
    start_urls = ["http://stackoverflow.com/questions?pagesize=50&sort=newest"]

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse(self, response):
        #item = BigscrapeItem()
        questions = Selector(response).xpath('//div[@class="summary"]/h3')
        for question in questions:
            item = BigscrapeItem()
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').get()
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').get()
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
            yield item
