import json
import requests

def working_hours(elem):
    '''
     ["пн - пт 10:00 до 20:00", "сб-вс 10:00-20:00"]
     elem = {
            "workdays": {
                "startStr": "11:00",
                "endStr": "21:00",
                "isDayOff": false
            },
            "saturday": {
                "startStr": "11:00",
                "endStr": "18:00",
                "isDayOff": false
            },
            "sunday": {
                "isDayOff": true
            }
        }
    '''
    # for i in working_hours.items():
    #     if i == 'workdays':
    #         k = working_hours.get("workdays")
    #         for m in k:
    #             working_hours_list["startStr_wd"] = m['startStr']
    #             working_hours_list["endStr_wd"] = m['endStr']
    #     elif i == 'saturday':
    #         l = working_hours.get("saturday")
    #         if len(l) > 1:
    #             for n in l:
    #                 working_hours_list["startStr_sun"] = l['startStr']
    #                 working_hours_list["endStr_sun"] = l['endStr']
    #         else:
    #             working_hours_list["startStr_sun"] = 'сб'
    #             working_hours_list["endStr_sun"] = 'выходной'
    #     elif i == 'sunday':
    #         k = working_hours.get("saturday")
    #         if len(k) > 1:
    #             for m in k:
    #                 working_hours_list["startStr_sat"] = m['startStr']
    #                 working_hours_list["endStr_sat"] = m['endStr']
    #         else:
    #             working_hours_list["startStr_sat"] = 'вс'
    #             working_hours_list["endStr_sat"] = 'выходной'
    pass

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
        phones = elem["phone"].split(';')
        working = working_hours(elem["hoursOfOperation"])

        result.append({
            "address": address,
            "latlon" : latlon,
            "name" : name,
            "phones" : None if not phones else phones,
            "working_hours": working
            # "working_hours" : f"пн-пт {working_hours_list['startStr_wd']}-{working_hours_list['endStr_wd']}, "
            #                   f"сб {working_hours_list['startStr_sun']}-{working_hours_list['endStr_sun']}, "
            #                   f"вс {working_hours_list['startStr_sat']}-{working_hours_list['endStr_sat']}"
            })
    for i in result:
        print(i)

    with open('tui_offices.json', 'w') as output_file:
        json.dump(result, output_file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    get_file()
