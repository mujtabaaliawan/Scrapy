import os
import schedule
import time


def main():
    schedule.every(2).minutes.do(os.system('scrapy crawl market'))
    print("Next Run at: ", schedule.next_run())

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
