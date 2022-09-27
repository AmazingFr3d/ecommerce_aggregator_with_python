from functions import locator as loc
from functions import extractor as ext


def main(keyword):
    output = []
    site_code = [1, 2, 3]

    for site in site_code:
        page_html = loc.html_parser(site, keyword)
        result = ext.extractor(site, page_html)
        output.append(result)

    return output
