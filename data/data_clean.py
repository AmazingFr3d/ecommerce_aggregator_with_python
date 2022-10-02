import pandas as pd
from functions import currency_conv as cc


def dataframes(site_code: int, data):
    if site_code == 1:
        aliexpress = pd.DataFrame.from_dict(data, orient='index').transpose()
        aliexpress['site'] = "amazon.com"
        aliexpress = aliexpress[aliexpress['name'].notnull()]

        return aliexpress

    elif site_code == 2:
        amazon = pd.DataFrame.from_dict(data, orient='index').transpose()
        amazon['site'] = "amazon.com"
        amazon = amazon[amazon['name'].notnull()]
        amazon['price'] = amazon['price'].str.replace('$', '')
        amazon['price'] = amazon['price'].str.replace(',', '')
        amazon['price'] = amazon['price'].str.replace(' ', '')
        amazon['price'] = amazon['price'].astype(float)
        amazon['price'] = amazon['price'] * cc.convert()
        amazon['price'] = amazon['price'].round(2)

        return amazon

    elif site_code == 3:
        jumia = pd.DataFrame.from_dict(data, orient='index').transpose()
        jumia['site'] = "jumia.com"
        jumia = jumia[jumia['name'].notnull()]
        jumia['price'] = jumia['price'].str.replace('₦', '')
        jumia['price'] = jumia['price'].str.replace(',', '')
        jumia['price'] = jumia['price'].str.replace(' ', '')
        jumia['price'] = jumia['price'].astype(float)

        return jumia
