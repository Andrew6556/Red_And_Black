import json


def read_json_file(file):
    with open(f'data/{file}', "r", encoding="utf-8") as read_file:
        data = json.load(read_file)
    return data

def write_json_file(file, data):
    with open(f'data/{file}', "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

