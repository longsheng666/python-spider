# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    area = scrapy.Field()
    room_id= scrapy.Field()
    room_name = scrapy.Field()
    room_url = scrapy.Field()
    introduction = scrapy.Field()
    space = scrapy.Field()
    community = scrapy.Field()
    floor = scrapy.Field()
    build_time = scrapy.Field()
    positionInfo = scrapy.Field()
    people_focus = scrapy.Field()
    look = scrapy.Field()
    publish_time = scrapy.Field()
    tag = scrapy.Field()
    price = scrapy.Field()
    unitprice = scrapy.Field()
    referer = scrapy.Field()




