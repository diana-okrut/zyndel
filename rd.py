import json
import requests
from lxml import etree
from lxml import html


def read_file():
    response = requests.get('https://www.mebelshara.ru/contacts')
    text = response.text
    # TODO: WTF?
    with open('test.html', 'wb') as output_file:
        output_file.write(text.encode('utf-8'))
    with open('test.html', 'rb') as input_file:
        text = input_file.read().decode('utf-8')
    return text


def parse_user_datafile_lxml():
    results = []
    text = read_file()

    tree = html.fromstring(text)

    adress_list_lxml = tree.xpath('//div[@class = "city-list js-city-list"]')[0]
    for item_lxml in adress_list_lxml:
        for element in item_lxml.xpath('.//div[@class = "shop-list-item"]'):
            name = element.get("data-shop-name")
            print(name)

        # TODO: use H4 tag only
        city = item_lxml.xpath('.//h4[@class = "js-city-name"]/text()')[0]
        shop_address = item_lxml.xpath('.//div[@class = "shop-address"]/text()')[0]
        shop_name = item_lxml.xpath('.//div[@class = "shop-name"]/text()')[0]
        phones = item_lxml.xpath('.//div[@class = "shop-phone"]/text()')[0]
        working_hours = item_lxml.xpath('.//div[@class = "shop-weekends"]/text()')[0]
        weekends = item_lxml.xpath('.//div[@class = "shop-work-time"]/text()')[0]
        wh = ','.join([working_hours, weekends]) if weekends != 'Без выходных:' else ','.join([working_hours])
        results.append({
            "address": ','.join([city, shop_address]),
            "latlon": None,
            "name": shop_name,
            "phones": phones,
            "working_hours": wh,
        })

    with open('test_file.json', 'w') as file:
        json.dump(results, file, indent=4)


if __name__ == "__main__":
    parse_user_datafile_lxml()
