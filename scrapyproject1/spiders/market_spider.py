import scrapy
from scrapyproject1.items import StockItem
from scrapy.loader import ItemLoader
from scrapyproject1.selectors import selectors


class StockSpider(scrapy.Spider):
    name = "market"
    start_urls = [selectors.MARKET_URL]


    def parse(self, response, **kwargs):

        field_to_index_mapping = [
            {'field_name': 'ldcp', 'index': 0},
            {'field_name': 'open', 'index': 1},
            {'field_name': 'high', 'index': 2},
            {'field_name': 'low', 'index': 3},
            {'field_name': 'current', 'index': 4},
            {'field_name': 'change', 'index': 6},
            {'field_name': 'volume', 'index': 7},
        ]

        market_date = response.css(selectors.DATE_BOARD)
        market_last_updated = market_date.css(selectors.DATE_ELEMENT).get()

        market_main_board = response.css(selectors.MARKET_BOARD)

        for table in market_main_board.css(selectors.CATEGORY_BOARD):

            category_name = table.css(selectors.CATEGORY_ELEMENT).extract()

            for company in table.css(selectors.COMPANY_BOARD):

                company_name = company.css(selectors.COMPANY_NAME_ELEMENT).extract()
                stock_detail = company.css(selectors.COMPANY_DATA_ELEMENT).extract()

                product = ItemLoader(item=StockItem())

                product.add_value('category', category_name)
                product.add_value('company', company_name)
                product.add_value('date_time', market_last_updated)

                for field_index_map in field_to_index_mapping:
                    product.add_value(field_index_map['field_name'], stock_detail[field_index_map['index']])

                yield product.load_item()
