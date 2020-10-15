import json

import requests
from lxml import html


def main():
    response = requests.get('https://www.mebelshara.ru/contacts')
    mebelshara_shops = []
    tree = html.fromstring(response.text)
    address_list_lxml = tree.xpath('//div[@class = "city-item"]')

    for item_lxml in address_list_lxml:
        city = item_lxml.xpath('.//h4[@class = "js-city-name"]/text()')[0]
        for element in item_lxml.xpath('.//div[@class = "shop-list-item"]'):
            address = element.get("data-shop-address")

            phone = element.get("data-shop-phone")

            weekend = element.get("data-shop-mode1")
            working = element.get("data-shop-mode2")
            working_hours = [f'пн - вс {working}'] if "Без" in weekend else [weekend, working]

            latitude = float(element.get("data-shop-latitude"))
            longitude = float(element.get("data-shop-longitude"))

            mebelshara_shops.append({
                "address": f'{city}, {address}',
                "latlon": [latitude, longitude],
                "name": "Мебель Шара",  # в ТЗ в поле name указано название магазина, а не название ТЦ
                "phones": None if not phone else phone.replace('(', '').replace(')', ''),
                "working_hours": working_hours
            })

    with open('mebelshara_shops.json', 'w') as file:
        json.dump(mebelshara_shops, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
