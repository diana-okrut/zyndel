import json
import requests


def read_file():
    response = requests.get('https://apigate.tui.ru/api/office/list?cityId=1&subwayId=&hoursFrom=&hoursTo=&serviceIds=all&toBeOpenOnHolidays=false')
    data = response.json()
    # TODO: clean the data
    result = []
    with open('test2.json', 'w') as output_file:
        json.dump(result, output_file, indent=2)


if __name__ == "__main__":
    read_file()
