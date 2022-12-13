import scrapy
from scrapyproject1.items import StockItem
from scrapy.loader import ItemLoader


class StockSpider(scrapy.Spider):
    name = "market"
    start_urls = [
        'https://www.psx.com.pk/market-summary/',
    ]

    def parse(self, response):

        market_date = response.css("div.col-sm-12.inner-content-table")
        market_last_updated = market_date.css("h4::text").get()

        market_main_board = response.css("#marketmainboard")
        for table in market_main_board.css("div.table-responsive"):

            category_name = table.css("h4::text").extract()
            company_data = table.css("tr td.dataportal")

            for company in company_data:
                price_data = company.css("td.dataportal ~ td::text").extract()
                product = ItemLoader(item=StockItem())
                product.add_value('category', category_name)
                product.add_value('company', company.css("::text").extract())
                product.add_value('ldcp', price_data[0])
                product.add_value('open', price_data[1])
                product.add_value('high', price_data[2])
                product.add_value('low', price_data[3])
                product.add_value('current', price_data[4])
                product.add_value('change', price_data[6])
                product.add_value('volume', price_data[7])
                product.add_value('date_time', market_last_updated)
                yield product.load_item()


