from functions import locator as loc
from functions import extractor as ext
from data import data_clean as df


def main(keyword):
    output = []
    site_code = [2, 3]

    for site in site_code:
        page_html = loc.html_parser(site, keyword)
        result = ext.extractor(site, page_html)
        data_frame = df.dataframes(site, result)
        output.append(data_frame)
    return output
