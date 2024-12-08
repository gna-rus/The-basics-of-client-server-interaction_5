# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# Модуль Items.py Нужен для упаковки данных
import scrapy

class JobparserItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field() # Обьявляю поля которые надо вытянуть из Паука (смотри hhru, эти переменные есть там)
    cost = scrapy.Field()
    url_items = scrapy.Field()



