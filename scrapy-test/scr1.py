# scr1.py
# Mikhail Kolodin, 2019
# python3, user virtualenv
# text from docs to make futher tests
# taken from scrapy.org, scrapinghub.com 
# https://www.youtube.com/watch?v=CsaqVQ4NIEU 
# youtube: Scrapy - Overview and Demo (web crawling and scraping) by Melvin L

import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}

        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)

