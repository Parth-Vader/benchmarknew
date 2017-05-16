#!/usr/bin/env python
# -*- coding: utf-8 -*-   
import re
from six.moves.urllib.parse import urlparse
#from datetime import datetime
import datetime
import scrapy
from scrapy.http import Request, HtmlResponse
from scrapy.linkextractors import LinkExtractor

from books.items import Page


class FollowAllSpider(scrapy.Spider):

    name = 'followall'
    ratings_map = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
    }

    def __init__(self, **kw):
        super(FollowAllSpider, self).__init__(**kw)
        url = kw.get('url') or kw.get('domain') or 'http://localhost/books.toscrape.com/index.html'
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://%s/' % url
        self.url = url
        self.allowed_domains = [re.sub(r'^www\.', '', urlparse(url).hostname)]
        self.link_extractor = LinkExtractor()
        self.cookies_seen = set()

    def start_requests(self):
        return [Request(self.url, callback=self.parse, dont_filter=True)]

    def parse(self, response):
        """Parse a PageItem and all requests to follow

        
        @url http://www.scrapinghub.com/
        @returns items 1 1
        @returns requests 1
        @scrapes url title foo
        """        
        page = self._get_item(response)
        r = [page]
        
        r.extend(self._extract_requests(response))
        items = self.crawler.stats.get_value('item_scraped_count', 0)
        pages = self.crawler.stats.get_value('response_received_count', 0)
        a = self.crawler.stats.get_value('start_time')
        b = datetime.datetime.now()
        c = b - datetime.timedelta(0,19800) # Done because my machine has a time zone problem
        
        timesec = c-a
        f=open("AvSpeed.txt",'w')
        f.write("{0}".format(int(items * (1/timesec.total_seconds()))))
        return r

    def _get_item(self, response):
        item = Page(
            url=response.url,
            size=str(len(response.body)),
            referer=response.request.headers.get('Referer'),
            rating = response.css('p.star-rating::attr(class)').extract_first().split(' ')[-1],
	        title = response.css('.product_main h1::text').extract_first(),
	        price = response.css('.product_main p.price_color::text').re_first('£(.*)'),
	        stock = ''.join(response.css('.product_main .instock.availability ::text').re('(\d+)')),
	        category = ''.join(response.css('ul.breadcrumb li:nth-last-child(2) ::text').extract()).strip(),
        )
        
        self._set_new_cookies(item, response)
        return item

        
    def _extract_requests(self, response):
        r = []
        if isinstance(response, HtmlResponse):
            links = self.link_extractor.extract_links(response)
            r.extend(Request(x.url, callback=self.parse) for x in links)
        return r

    def _set_new_cookies(self, page, response):
        cookies = []
        for cookie in [x.split(b';', 1)[0] for x in
                       response.headers.getlist('Set-Cookie')]:
            if cookie not in self.cookies_seen:
                self.cookies_seen.add(cookie)
                cookies.append(cookie)
        if cookies:
            page['newcookies'] = cookies
