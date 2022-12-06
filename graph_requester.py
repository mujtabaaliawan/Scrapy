import json
import requests


def main():

    data = {
        "company_id": 1,
        "from_datetime": "2022-12-06 13:05:25",
        "to_datetime": "2022-12-06 18:50:25"
    }

    json_data = json.dumps(data)

    URL = "http://127.0.0.1:8000/graph"
    header = {'Content-type': 'application/json'}
    graph_json_data = requests.post(url=URL, data=json_data, headers=header)
    graph_data = json.loads(graph_json_data.content)
    print(graph_data)


if __name__ == '__main__':
    main()
