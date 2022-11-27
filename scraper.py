import scrapy


class Spider(scrapy.Spider):
    name = 'scraper'
    allowed_domains = ['first-buggy.ru']
    start_urls = ['https://www.first-buggy.ru/catalog/%D0%94%D0%B5%D1%82%D1%81%D0%BA%D0%B8%D0%B5-%D0%BA%D0%BE%D0%BB%D1%8F%D1%81%D0%BA%D0%B8/']

    def parse(self, response):

        price = response.css('span.cur-price::text').getall()
        descr = response.css('div.descr').getall()
        d = descr.css('p::text').getall()
        print(dict(price=price, description=d))

        for item in zip(price, d):
            yield {
                'Цена': item[0],
                'Описание': item[1],
        }

