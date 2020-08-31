# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class JiaoyimaoItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    title = scrapy.Field()
    server_name = scrapy.Field()
    category_name = scrapy.Field()
    price = scrapy.Field()
    favorite_count = scrapy.Field()
    pass
