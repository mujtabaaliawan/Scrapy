import scrapy
from itemloaders.processors import TakeFirst, MapCompose


def to_float(value):
    value = value.replace(',', '')
    return float(value)


def to_int(value):
    value = value.replace(',', '')
    return int(value)


def stripper(value):
    return value.strip()


class StockItem(scrapy.Item):
    category = scrapy.Field(
        input_processor=MapCompose(stripper),
        output_processor=TakeFirst()
    )
    company = scrapy.Field(
        input_processor=MapCompose(stripper),
        output_processor=TakeFirst()
    )
    ldcp = scrapy.Field(
        input_processor=MapCompose(to_float),
        output_processor=TakeFirst()
    )
    open = scrapy.Field(
        input_processor=MapCompose(to_float),
        output_processor=TakeFirst()
    )
    high = scrapy.Field(
        input_processor=MapCompose(to_float),
        output_processor=TakeFirst()
    )
    low = scrapy.Field(
        input_processor=MapCompose(to_float),
        output_processor=TakeFirst()
    )
    current = scrapy.Field(
        input_processor=MapCompose(to_float),
        output_processor=TakeFirst()
    )
    change = scrapy.Field(
        input_processor=MapCompose(to_float),
        output_processor=TakeFirst()
    )
    volume = scrapy.Field(
        input_processor=MapCompose(to_int),
        output_processor=TakeFirst()
    )
    date_time = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=TakeFirst()
    )
