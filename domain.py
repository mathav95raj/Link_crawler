# -*- coding: utf-8 -*-
from urllib.parse import urlparse


#get domain name(example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''
#get sub domain name(mail.name.example.com)

def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

#print(get_domain_name('https://mail.google.com/mail/?tab=rm&authuser=0&ogbl'))