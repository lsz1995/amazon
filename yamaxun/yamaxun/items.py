# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YamaxunItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ID=scrapy.Field()
    name=scrapy.Field()
    price=scrapy.Field()
    score=scrapy.Field()
    comments_total=scrapy.Field()
    comment_data=scrapy.Field()


