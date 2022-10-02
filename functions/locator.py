from playwright.sync_api import sync_playwright

import time

from functions import url_builder as ub


def html_parser(site_code: int, keyword: str):

    url = ub.url_builder(site_code, keyword)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport={"width": 1920, "height": 1080})

        page = browser.new_page()

        page.goto(url, wait_until="domcontentloaded")
        # page.wait_for_selector(selector_wait)  # wait for content to load

        # page.mouse.wheel(horizontally, vertically(positive is
        # scrolling down, negative is scrolling up)
        for i in range(2):  # make the range as long as needed
            page.mouse.wheel(0, 15000)
            time.sleep(2)
            i += 1
        time.sleep(2)
        for i in range(2):  # make the range as long as needed
            page.mouse.wheel(0, -15000)
            time.sleep(2)
            i += 1
        time.sleep(2)
        # ---------------------
        html = page.content()
        browser.close()

        return html
