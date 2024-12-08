import scrapy
from scrapy.http import HtmlResponse # Импортирую методы типа HtmlResponse
from scrapy_project.items import JobparserItem # привязываю Паука к items.py


class HhruSpider(scrapy.Spider):
    name = "hhru"
    domen = 'foroffice.ru'
    allowed_domains = [domen] # Указываем списко доменов на которые может ходить паук
    start_urls = ["https://www.foroffice.ru/products/ploskie-termopressy.html"] # Точка входа

    # При запуске паука, автоматически осуществляется get запрос на каждую ссылку что представлена в start_urls и
    # будет получен response, который автоматически передается в def parse

    def correct_info(self, text):
        """
        :param text: информация о тексте вытащеная с сайта, в виде списка
        :return: цену в виде str
        """
        list_value = []
        result = ''
        for i in text:
            list_value.append(i.replace(" ", ""))
        for i in list_value:
            for j in i:
                if j in '1234567890Р':
                    if j == 'Р':
                        result += " " + "Р"
                    else:
                        result += j
        if result.count('Р') > 1:
            nomber = result.find('Р')
            text = '' + result[:nomber + 1] + ' - ' + result[nomber + 1:]
            result = text

        return result

    def parse(self, response: HtmlResponse): # присваиваю response тип HtmlResponse для возможности применять методы HtmlResponse
        # обработка всей страницы и переход на вложенные страницы

        links = response.xpath("//div[@class='image-block']//a/@href").getall() # возвращает список ссылок всех атрибутов страницы по xpath
        print(response.status, response.url)
        print(links)
        for link in links:
            link = 'https://www.foroffice.ru/'+link # генерирую ссылку для перехода
            yield response.follow(link, callback=self.vacancy_parse) # follow - можно сказать это функция для перехода по ссылке. В рамках единой ссесии получаю ссылку и перехожу по ссылке (yield обязателен при большом количестве запросов)

        next_page = response.xpath('//button[@aria-label="Go to next page"]') # переход на следующую страницу (xpath кнопки)
        if next_page: # проверка на то что есть следущая страница
            yield response.follow(next_page, callback=self.parse) # програжую следущую страницу но при этом рекурсивно обращение на самого себя

    def vacancy_parse(self, response: HtmlResponse):
        name = response.xpath("//h1[@class='mb-0']//text()").getall()
        cost = response.xpath("//div[@class='prc']//text()").getall()
        url_items = response.url
        print(cost)
        cost = self.correct_info(cost)
        print(1, name, cost, url_items)
        yield JobparserItem(name=name, cost=cost, url_items=url_items) # отправляем данные в items.py

