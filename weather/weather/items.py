# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # demo 1
    city = scrapy.Field()
    date = scrapy.Field()
    day = scrapy.Field()
    dayDesc = scrapy.Field()
    dayTemp = scrapy.Field()
    night = scrapy.Field()
    nightDesc = scrapy.Field()
    nightTemp = scrapy.Field()
    tip = scrapy.Field()
    pass
