from bs4 import BeautifulSoup
from lxml import etree

from functions import selectors as sel


def extractor(site_code: int, page_html: str):
    """
     This function accepts the page html along with specific selectors and returns
     a list of dict of all the scraped products

     prod_html: this is the entire html of the site.

     prods_select: this the selector for the list of products from the site.

     name: this is the selector for the product name, to be used in the loop.

     price: this is the selector for the product price, to be used in the loop.

     stars: this is the selector for the product rating stars, to be used in the loop.

     img: this is the selector for the product image url, to be used in the loop.

     urls: this is the selector for the product url, to be used in the loop.

     Note all selector should be in xpath

    """

    soup = BeautifulSoup(page_html, 'html.parser')
    dom = etree.HTML(str(soup))
    parsed = []
    i = 0
    prods_select = sel.selectors(site_code)
    products = dom.xpath(prods_select['prods'])
    for product in products:
        i += 1
        result = {
            'Name': product.xpath(prods_select['name']),
            'Price': " ".join(product.xpath(prods_select['price'])),
            'Stars': product.xpath(prods_select['stars']),
            # 'img_url': product.xpath(prods_select['img']),
            # 'url': product.xpath(prods_select['url']),
            'Platform': product.xpath(prods_select['platform'])
        }
        parsed.append(result)
        if i == 15:
            break
    return parsed
