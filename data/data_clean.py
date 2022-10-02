import pandas as pd


def dataframes(site_code: int, data):
    if site_code == 1:
        aliexpress = pd.DataFrame.from_dict(data, orient='index').transpose()
        aliexpress['site'] = "amazon.com"
        aliexpress.dropna()
        return aliexpress[aliexpress['name'].notnull()]

    elif site_code == 2:
        amazon = pd.DataFrame.from_dict(data, orient='index').transpose()
        amazon['site'] = "amazon.com"

        return amazon[amazon['name'].notnull()]

    elif site_code == 3:
        jumia = pd.DataFrame.from_dict(data, orient='index').transpose()
        jumia['site'] = "jumia.com"

        return jumia[jumia['name'].notnull()]
