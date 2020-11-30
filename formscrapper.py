import pandas as pd
from bs4 import BeautifulSoup as bs
import requests as r
import re
import csv

url = ''
soup = bs(r.get(url).content, "lxml")
cont = soup.find_all(
    "div", {"class": "freebirdFormviewerComponentsQuestionGridCell freebirdFormviewerComponentsQuestionGridRowHeader"})
cont = cont[1:]

comps = [x.string for x in cont]

city = pd.DataFrame(comps)
city.to_csv('1_4.csv')
