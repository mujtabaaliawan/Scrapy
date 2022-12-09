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

        for table in response.css("div.table-responsive"):

            category_name = table.css("h4::text").extract()
            company_data = table.css("td.dataportal::text").extract()
            price_data = table.css("td.dataportal ~ td::text").extract()
            i = 0
            for company in company_data:
                product = ItemLoader(item=StockItem())
                product.add_value('category', category_name)
                product.add_value('company', company)
                product.add_value('ldcp', price_data[i])
                product.add_value('open', price_data[i+1])
                product.add_value('high', price_data[i+2])
                product.add_value('low', price_data[i+3])
                product.add_value('current', price_data[i+4])
                product.add_value('change', price_data[i+6])
                product.add_value('volume', price_data[i+7])
                i = i + 8
                product.add_value('date_time', market_last_updated)
                yield product.load_item()


