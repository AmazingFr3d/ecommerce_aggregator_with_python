from functions import locator as loc
from functions import extractor as ext

item = "Arduino Uno"
selector = ".product-card"
url = "https://www.aliexpress.com/af/raspberry-pi.html"

page_html = loc.html_parser(item, url, selector)

prods = "//a[@class='_3t7zg _2f4Ho']"
name = "//div[2]/div[1]/h1/text()"
price = "//div[2]/div[2]/span/text()"
stars = "//div[2]/div[4]/span[2]"
img = "//div/img/@src"
url = "//@href"

print(ext.extractor(page_html, prods, name, price, stars, img, url))
