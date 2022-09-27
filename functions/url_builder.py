def url_builder(site_code: int, keyword: str):

    if site_code == 1:  # 1 is for Aliexpress.com

        # this line prepare the search keyword to be injected into the url
        keyword = keyword.replace(" ", "-")

        # This line injects the keywords into the url and assigns it to url variable
        url = f"https://www.aliexpress.com/af/{keyword}.html"

    if site_code == 2:  # 2 is for Amazon.com

        # this line prepare the search keyword to be injected into the url
        keyword = keyword.replace(" ", "+")

        # This line injects the keywords into the url and assigns it to url variable
        url = f"https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords={keyword}"

    if site_code == 3:  # 3 is for Jumia.com

        # this line prepare the search keyword to be injected into the url
        keyword = keyword.replace(" ", "+")

        # This line injects the keywords into the url and assigns it to url variable
        url = f"https://www.jumia.com.ng/catalog/?q={keyword}"

    return url
