import scrapy
from scrapyproject1.items import StockItem
from scrapy.loader import ItemLoader


class StockSpider(scrapy.Spider):
    name = "market"
    start_urls = [
        'https://www.psx.com.pk/market-summary/',
    ]

    def parse(self, response):

        market_date = response.css("div.inner-content-table")
        market_last_updated = market_date.css("h4::text").get()
        market_main_board = response.css("div.active")

        for table in market_main_board.css("div.table-responsive"):

            category_name = table.css("h4::text").extract()
            company_data = table.css("tr td.dataportal")

            for company in company_data:
                stock_detail = company.css("td.dataportal ~ td::text").extract()
                product = ItemLoader(item=StockItem())
                product.add_value('category', category_name)
                product.add_value('company', company.css("::text").extract())
                product.add_value('ldcp', stock_detail[0])
                product.add_value('open', stock_detail[1])
                product.add_value('high', stock_detail[2])
                product.add_value('low', stock_detail[3])
                product.add_value('current', stock_detail[4])
                product.add_value('change', stock_detail[6])
                product.add_value('volume', stock_detail[7])
                product.add_value('date_time', market_last_updated)
                yield product.load_item()


