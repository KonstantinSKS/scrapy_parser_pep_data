import scrapy


class PepParseItem(scrapy.Item):
    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
