import json
import requests


def main():

    URL = "http://127.0.0.1:8000/graph?company=1&date_time_lt=2022-12-06 13:05:25&date_time_gt=2022-12-13 18:50:25"
    response = requests.get(url=URL)
    print(response.content)


if __name__ == '__main__':
    main()
