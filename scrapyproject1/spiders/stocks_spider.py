import scrapy
from scrapyproject1.items import StockItem
from scrapy.loader import ItemLoader


class StockSpider(scrapy.Spider):
    name = "stock"
    start_urls = [
        'https://www.psx.com.pk/market-summary/',
    ]
    custom_settings = {
        "FEEDS": {
            "stocks.json": {"format": "json"},
        },
    }

    def parse(self, response):
        market_date = response.css("div.col-sm-12.inner-content-table")
        market_last_updated = market_date.css("h4::text").get()
        market_content = response.css("div.tab-content")
        market_main_board = market_content.css("div.col-sm-12.tab-pane.inner-content-table.automobile-div.active")

        for table in market_main_board.css("div.table-responsive"):

            category_name = table.css("h4::text").get()

            for stock_item in table.css("tr.red-text-td"):
                item_data = stock_item.css("td::text").getall()

                product = ItemLoader(item=StockItem())
                product.add_value('category', category_name)
                product.add_value('company', item_data[0])
                product.add_value('ldcp', item_data[1])
                product.add_value('open', item_data[2])
                product.add_value('high', item_data[3])
                product.add_value('low', item_data[4])
                product.add_value('current', item_data[5])
                product.add_value('change', item_data[7])
                product.add_value('volume', item_data[8])
                product.add_value('date', market_last_updated)
                yield product.load_item()

            for stock_item in table.css("tr.blue-text-td"):
                item_data = stock_item.css("td::text").getall()

                product = ItemLoader(item=StockItem())
                product.add_value('category', category_name)
                product.add_value('company', item_data[0])
                product.add_value('ldcp', item_data[1])
                product.add_value('open', item_data[2])
                product.add_value('high', item_data[3])
                product.add_value('low', item_data[4])
                product.add_value('current', item_data[5])
                product.add_value('change', item_data[7])
                product.add_value('volume', item_data[8])
                product.add_value('date', market_last_updated)
                yield product.load_item()

            for stock_item in table.css("tr.green-text-td"):
                item_data = stock_item.css("td::text").getall()

                product = ItemLoader(item=StockItem())
                product.add_value('category', category_name)
                product.add_value('company', item_data[0])
                product.add_value('ldcp', item_data[1])
                product.add_value('open', item_data[2])
                product.add_value('high', item_data[3])
                product.add_value('low', item_data[4])
                product.add_value('current', item_data[5])
                product.add_value('change', item_data[7])
                product.add_value('volume', item_data[8])
                product.add_value('date', market_last_updated)
                yield product.load_item()
