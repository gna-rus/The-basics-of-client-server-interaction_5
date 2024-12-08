# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json

class ScrapyProjectPipeline:
    def process_item(self, item, spider):
        return item# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

# Модуль pipelines.py принимает упакованные данные из items.py и проводит фиксацию данных (отправляет данные куда либо или загружает данные в файл)

from pymongo import MongoClient

class JobparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017) # Инициализирую подключение к БД
        self.mongo_base = client.items05122024 # создаю БД в Манго


    def process_item(self, item, spider):
        print(item)

        dict1 = {}
        dict1[item['name'][0]] = [item['cost'], item['url_items']]

        # Добавляю данные в json
        with open('result.json', 'a', encoding='utf-8') as file:
            json.dump(dict1, file, ensure_ascii=False, indent=4)
            file.write(',\n')

        return item

