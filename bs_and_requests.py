# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 22:21:55 2020

@author: cosmotron
"""

from bs4 import BeautifulSoup as bs
import requests as r
from urllib.parse import urlparse, urljoin

internal_urls = set()
external_urls = set()

def is_valid(url):
    parsed = urlparse(url)
    if (parsed[0] == 'javascript'):
        return False
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_website_links(url):
    urls = set()
#    domain_name = urlparse(url).netloc
    soup = bs(r.get(url).content, "lxml")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            continue
        urls.add(href)
    return urls

total_urls_visited = 0

def crawl(url, max_urls=50):
    global total_urls_visited
    total_urls_visited += 1
    links = get_all_website_links(url)
    for link in links:
        print(link)
    for link in links:
        if total_urls_visited > max_urls:
            break
        crawl(link, max_urls=max_urls)
        
url = "https://flinkhub.com/"
crawl(url)
