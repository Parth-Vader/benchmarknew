#!/usr/bin/env python
# -*- coding: utf-8 -*-   
import re
from six.moves.urllib.parse import urlparse

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

    default_settings = {
        'LOG_LEVEL': 'INFO',
        'LOGSTATS_INTERVAL': 1,
        'CLOSESPIDER_TIMEOUT': 10,
	}    

    def start_requests(self):
        return [Request(self.url, callback=self.parse, dont_filter=True)]

    def parse(self, response):
        """Parse a PageItem and all requests to follow

        
        @url http://www.scrapinghub.com/
        @returns items 1 1
        @returns requests 1
        @scrapes url title foo
        """
        '''
        rating = response.css('p.star-rating::attr(class)').extract_first().split(' ')[-1]
        yield {
            'rating': self.ratings_map.get(rating.lower(), ''),
            'title': response.css('.product_main h1::text').extract_first(),
           
            'stock': int(
                ''.join(
                    response.css('.product_main .instock.availability ::text').re('(\d+)')
                )
            ),
            'category': ''.join(
                response.css('ul.breadcrumb li:nth-last-child(2) ::text').extract()
            ).strip(),
        }
        '''
        items = self.crawler.stats.get_value('item_scraped_count', 0)
        pages = self.crawler.stats.get_value('response_received_count', 0)
        
        f=open("AvSpeed.txt",'w')
        f.write("{0}".format(items*2))
        page = self._get_item(response)
        r = [page]
        #print(r)
        r.extend(self._extract_requests(response))
        return r

        

    def _get_item(self, response):
        item = Page(
            url=response.url,
            size=str(len(response.body)),
            referer=response.request.headers.get('Referer'),
        )
        rating = response.css('p.star-rating::attr(class)').extract_first().split(' ')[-1]
        title = response.css('.product_main h1::text').extract_first()
        price = response.css('.product_main p.price_color::text').re_first('£(.*)')
        stock = ''.join(response.css('.product_main .instock.availability ::text').re('(\d+)'))
        category = ''.join(response.css('ul.breadcrumb li:nth-last-child(2) ::text').extract()).strip()
        
        self._set_title(item, response)
        self._set_new_cookies(item, response)
        
        return item

        
    def _extract_requests(self, response):
        r = []
        if isinstance(response, HtmlResponse):
            links = self.link_extractor.extract_links(response)
            r.extend(Request(x.url, callback=self.parse) for x in links)
        return r

    def _set_title(self, page, response):
        if isinstance(response, HtmlResponse):
            title = response.xpath("//title/text()").extract()
            if title:
                page['title'] = title[0]

    def _set_new_cookies(self, page, response):
        cookies = []
        for cookie in [x.split(b';', 1)[0] for x in
                       response.headers.getlist('Set-Cookie')]:
            if cookie not in self.cookies_seen:
                self.cookies_seen.add(cookie)
                cookies.append(cookie)
        if cookies:
            page['newcookies'] = cookies
