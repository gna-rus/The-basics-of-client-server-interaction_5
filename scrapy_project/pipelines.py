# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


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
        print()
        # item.get('cost')
        # item
        collections = self.mongo_base[spider.name] # spider.name - подтягивает имя паука (может быть много пауков и чтобы их корректно в Моного они загрузились)
        collections.insetr_one(item )
        return item

