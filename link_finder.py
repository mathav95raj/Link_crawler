# -*- coding: utf-8 -*-
from urllib.request import urlopen
from html.parser import HTMLParser
from urllib import parse
from bs4 import BeautifulSoup as bs
import requests as r
from urllib.parse import urlparse, urljoin


class linkfinder():

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        print(self.base_url)
        self.links = set()
        self.extract_links()
        # print(base_url, page_url)

    @staticmethod
    def is_valid(url):
        parsed = urlparse(url)
        if (parsed[0] == 'javascript'):
            return False
        return bool(parsed.netloc) and bool(parsed.scheme)

    def extract_links(self):
        soup = bs(r.get(self.page_url).content, "lxml")
        for a_tag in soup.findAll("a"):
            href = a_tag.attrs.get("href")
            if href == "" or href is None:
                continue
            href = urljoin(self.base_url, href)
            parsed_href = urlparse(href)
            href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
            if not self.is_valid(href):
                continue
            self.links.add(href)
        # print(self.links)

    def page_links(self):
        return self.links

    def error(self, message):
        pass


# base_url = "https://sondernyonder.wordpress.com/"
# page_url = "https://sondernyonder.wordpress.com/"

#     return set()
# finder = linkfinder(base_url, page_url)
# finder.feed('<html><head><title>Flinkhub Projects</title>'
#             '<body><h1>Parse me</h1></body></html>')


# def gather_links(page_url):
#     # html_string = ''
#     # try:
#     #     response = urlopen(page_url)
#     #     if response.getheader('content type') == 'text/html':
#     #         html_bytes = response.read()
#     #         html_string = html_bytes.decode('utf-8')
#     finder = linkfinder(base_url, page_url)
#     # except:
#     #     print('error: cannot crawl page')
#     #     return set()
#     return finder.page_links()


# print(gather_links(page_url))
