from playwright.sync_api import sync_playwright


def html_parser(item: str, url: str, selector_wait: str):

    # this line prepare the search keyword to be injected into the url
    # item = item.replace(" ", "-")

    # This line injects the keywords into the url and assigns it to url variable
    # url = f"https://www.aliexpress.com/af/{item}.html"
    print(url)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport={"width": 1920, "height": 1080})

        page = browser.new_page()

        page.goto(url)
        page.wait_for_selector(selector_wait)  # wait for content to load

        browser.close()

        return page.content()
