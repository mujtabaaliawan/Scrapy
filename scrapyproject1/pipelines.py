from itemadapter import ItemAdapter
import json
import requests


class StockPipeline:

    def __init__(self):
        self.market = []

    def process_item(self, item, spider):
        self.market.append(ItemAdapter(item).asdict())
        return item

    def close_spider(self, spider):

        json_data = json.dumps(self.market)

        URL = "http://127.0.0.1:8000/handler"
        header = {'Content-type': 'application/json',
                  'Secret-Token': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtYXJrZXQiOiJzdG9jayIsIm5hbWUiOiJqYW5nb19yYW5nbyIsImNpdHkiOiJrYXJhY2hpIiwiaWF0IjoxNTE2MjM5MDIyfQ.-9ijMMtccWA_0NhGfDIPsJWYUYOJuKtE9P7U6-iovDI"}
        response = requests.post(url=URL, data=json_data, headers=header)
        print(response)

