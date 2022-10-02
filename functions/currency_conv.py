import requests
from bs4 import BeautifulSoup
from lxml import etree


def convert():
    url = "https://www.google.com/search?q=usd+to+ngn"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    dom = etree.HTML(str(soup))

    rate = dom.xpath("//div[@class='BNeawe iBp4i AP7Wnd']/text()")
    str_list = rate[0].split()
    rate = float(str_list[0])

    return rate
