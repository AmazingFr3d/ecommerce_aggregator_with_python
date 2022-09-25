from bs4 import BeautifulSoup
from lxml import etree


def extractor(page_html, prods_select: str, name: str, price: str, stars: str, img: str, url: str):
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
    products = dom.xpath(prods_select)
    for product in products:
        parsed.append({
            'Name': product.xpath(name),
            'Price': product.xpath(price),
            'Stars': product.xpath(stars),
            'img_url': product.xpath(img),
            'url': product.xpath(url)
        })
    return parsed
