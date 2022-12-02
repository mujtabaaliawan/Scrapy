import schedule
import time
import os


def main():
    print('Scheduler initialised')
    schedule.every(5).minutes.do(lambda: os.system('scrapy crawl stock'))
    schedule.every(330).seconds.do(lambda: os.system('python file_reader.py'))
    print('Next spider is set to run at: ' + str(schedule.next_run()))

    while True:
        schedule.run_pending()
        time.sleep(1)




if __name__ == '__main__':
    main()