import scrapy

from urllib.parse import urljoin

from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_NAME, PEP_ALLOWED_DOMAINS, PEP_START_URLS


class PepSpider(scrapy.Spider):
    name = PEP_NAME
    allowed_domains = PEP_ALLOWED_DOMAINS
    start_urls = PEP_START_URLS

    def parse(self, response):
        pep_links = response.css(
            '#numerical-index  tbody > tr > td > a::attr(href)').getall()
        for pep_link in pep_links:
            full_pep_link = urljoin(response.url, pep_link)
            yield response.follow(full_pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'number': response.css(
                '#pep-content > h1::text').re_first(r'PEP (\d+)'),
            'name': response.css(
                '#pep-content > h1::text').re_first(r'– (.+)'),
            'status': response.css(
                'dt:contains("Status") + dd > abbr::text').get()
        }
        yield PepParseItem(data)
