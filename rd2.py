import json

import requests


def working_hours(work_week):
    workdays, saturday, sunday = work_week['workdays'], work_week['saturday'], work_week['sunday']
    time_in_workdays = f"пн-пт {workdays['startStr']} до {workdays['endStr']}"
    time_in_sunday = None
    if sunday == saturday and len(sunday) > 1:
        time_in_weekend = f"сб-вс {saturday['startStr']} до {saturday['endStr']}"
    elif sunday == saturday and len(sunday) == 1:
        time_in_weekend = 'сб-вс выходной'
    elif sunday != saturday and len(sunday) == 1:
        time_in_weekend = f"сб {saturday['startStr']} до {saturday['endStr']}"
    else:
        time_in_weekend = f"сб {saturday['startStr']} до {saturday['endStr']}"
        time_in_sunday = f"вс {sunday['startStr']} до {sunday['endStr']}"
    result = [time_in_workdays, time_in_weekend] if not time_in_sunday \
        else [time_in_workdays, time_in_weekend, time_in_sunday]
    return result


def main():
    response = requests.get(
        'https://apigate.tui.ru/api/office/list?cityId=1&subwayId=&hoursFrom=&hoursTo=&serviceIds=all&toBeOpenOnHolidays=false')
    info_about_offices = json.loads(response.text)
    offices_list = info_about_offices.get('offices')
    result = []
    for office in offices_list:
        address = office["address"]
        latlon = [office["latitude"], office["longitude"]]
        name = office["name"]
        phones = office["phone"].split(';')
        working = working_hours(office["hoursOfOperation"])

        result.append({
            "address": address,
            "latlon": latlon,
            "name": name,
            "phones": None if not phones else phones,
            "working_hours": working
        })

    with open('tui_offices.json', 'w') as output_file:
        json.dump(result, output_file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
