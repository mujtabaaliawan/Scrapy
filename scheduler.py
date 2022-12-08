import schedule
import time
import os
import json
import requests
import schedule
import time


def main():
    schedule.every(1).minutes.do(start_scrapping)
    print("Next Run at: ", schedule.next_run())

    while True:
        schedule.run_pending()
        time.sleep(1)


def start_scrapping():
    os.system('scrapy crawl stock')
    data_sender()


def data_sender():
    if os.stat("stocks.json").st_size == 0:
        return
    with open('stocks.json', 'r') as openfile:
        data = json.load(openfile)
    json_data = json.dumps(data)
    with open('stocks.json', 'w') as openfile:
        pass
    URL = "http://127.0.0.1:8000/handler"
    header = {'Content-type': 'application/json',
              'Secret-Token': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtYXJrZXQiOiJzdG9jayIsIm5hbWUiOiJqYW5nb19yYW5nbyIsImNpdHkiOiJrYXJhY2hpIiwiaWF0IjoxNTE2MjM5MDIyfQ.-9ijMMtccWA_0NhGfDIPsJWYUYOJuKtE9P7U6-iovDI"}
    response = requests.post(url=URL, data=json_data, headers=header)
    print(response)

if __name__ == '__main__':
    main()
