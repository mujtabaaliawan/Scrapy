import json
import requests


def main():

    with open('stocks.json', 'r') as openfile:
        data = json.load(openfile)
    json_data = json.dumps(data)
    with open('stocks.json', 'w') as openfile:
        pass
    URL = "http://127.0.0.1:8000/handler"
    header = {'Content-type': 'application/json'}
    res = requests.post(url=URL, data=json_data, headers=header)
    print(res)

if __name__ == '__main__':
    main()
