import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_links = response.css(
            '#numerical-index  tbody > tr > td > a::attr(href)').getall()
        for pep_link in pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('#pep-content > h1::text').get().split(' – ')
        data = {
            'number': title[0][4:],
            'name': title[1],
            'status': response.css(
                'dt:contains("Status") + dd > abbr::text').get()
        }
        yield PepParseItem(data)
