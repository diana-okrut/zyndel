import json
import requests
from lxml import etree, html


def get_file():
    response = requests.get('https://www.mebelshara.ru/contacts')
    text = response.text
    return text


def parse_shops():
    mebelshara_shops = []
    text = get_file()
    tree = html.fromstring(text)

    adress_list_lxml = tree.xpath('//div[@class = "city-item"]')

    for item_lxml in adress_list_lxml:
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
                "address": f' {city}, {address}',
                "latlon": [latitude, longitude],
                "name": "Мебель Шара",
                "phones": None if not phone else [''.join(el for el in phone if el not in['(', ')'])],
                "working_hours": working_hours
            })

    with open('mebelshara_shops.json', 'w') as file:
        json.dump(mebelshara_shops, file, indent=4)


if __name__ == "__main__":
    parse_shops()
