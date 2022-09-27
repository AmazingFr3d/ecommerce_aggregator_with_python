def selectors(site_code: int):
    if site_code == 1:  # For Aliexpress.com
        details = {
            'prods': "//a[@class='_3t7zg _2f4Ho']",
            'name': "//a[@class='_3t7zg _2f4Ho']/div[2]/div[1]/h1/text()",
            'price': "//a[@class='_3t7zg _2f4Ho']/div[2]/div[2]/span/text()",
            'stars': "//a[@class='_3t7zg _2f4Ho']/div[2]/div[4]/span[2]",
            'img': "//a[@class='_3t7zg _2f4Ho']/div/img/@src",
            'url': "//a[@class='_3t7zg _2f4Ho']/@href",
            'platform': "aliexpress.com"
        }
        return details
    elif site_code == 2:  # For Amazon.com
        details = {
            'prods': "//div[@data-component-type='s-search-result']",
            'name': "//div[@data-component-type='s-search-result']//span[@class='a-size-medium a-color-base a-text-normal']",
            'price': "//div[@data-component-type='s-search-result']//span[@class='a-offscreen xh-highlight']",
            'stars': "//div[@data-component-type='s-search-result']//span[@class='a-icon-alt']",
            'img': "//div[@data-component-type='s-search-result']//img",
            'url': "//div[@data-component-type='s-search-result']//a[@class='a-link-normal s-no-outline']/@href",
            'platform': "amazon.com"
        }
        return details
    elif site_code == 3:  # For Jumia.com
        details = {
            'prods': "//article[@class='prd _fb col c-prd']",
            'name': "//article[@class='prd _fb col c-prd']//h3[@class='name']/text()",
            'price': "//article[@class='prd _fb col c-prd']//div[@class='prc']/text()",
            'stars': "//article[@class='prd _fb col c-prd']//div[@class='stars _s']/text()",
            'img': "//article[@class='prd _fb col c-prd']//img[@class='img']/@src",
            'url': "//article[@class='prd _fb col c-prd']//a[@class='core']/@href",
            'site': "jumia.com"
        }
        return details

