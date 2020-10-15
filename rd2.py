import json
import requests


def get_file():
    response = requests.get('https://apigate.tui.ru/api/office/list?cityId=1&subwayId=&hoursFrom=&hoursTo=&serviceIds=all&toBeOpenOnHolidays=false')
    data = response.json()
    offices = json.loads(response.text)
    a = offices.get('offices')
    result = []
    for elem in a:
        address = elem["address"]
        latlon = [elem["latitude"], elem["longitude"]]
        name = elem["name"]
        phones = elem["phone"]
        working_hours = elem["hoursOfOperation"]
        for i in working_hours.items():
            if i == 'workdays':
                k = working_hours.get(workdays)
            for k in workdays:

                startStr_wd = k['startStr']
                endStr_wd = k['endStr']
        elif i == 'saturday':
            k = working_hours.get(workdays)

            for m in workdays:
                startStr_sat = m['startStr']
                endStr_sat = m['endStr']
            sunday = i['sunday']
        result.append({
        "address": address,
        "latlon" : latlon,
        "name" : name,
        "phones" : phones,
        "working_hours" : f'пн-пт {startStr_wd}-{endStr_wd}, сб {startStr_sat}-{endStr_sat}, вс {sunday}'
        })
    for i in result:
        print(i)

    with open('tui_office.json', 'w') as output_file:
        json.dump(data, output_file, indent=4)


if __name__ == "__main__":
    get_file()
