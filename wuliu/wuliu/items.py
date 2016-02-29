# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhwlwItem(scrapy.Item):
    name = scrapy.Field()
    address = scrapy.Field()
    phone = scrapy.Field()
    telephone = scrapy.Field()
    email = scrapy.Field()
    pass
