import bs4
import requests


def price_check():
    # https://www.scorptec.com.au/product/hard-drives-&-ssds/hdd-3.5-drives/96004-st8000dx001

    # <div class="product-page-price product-main-price" style="text-align: right;">329</div>

    page = requests.get(
        "https://www.scorptec.com.au/product/hard-drives-&-ssds/hdd-3.5-drives/96004-st8000dx001",
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )
    soup = bs4.BeautifulSoup(page.text, "html.parser")

    # get price as an integer
    price = soup.find(
        "div", {"class": "product-main-price"}).text

    print("Firecuda 8TB at Scorptec is now " + price)

    if price != "329":
        print("Price has changed!")
        return "Price has changed! Firecuda 8TB at Scorptec is now " + \
            price + \
            " https://www.scorptec.com.au/product/hard-drives-&-ssds/hdd-3.5-drives/96004-st8000dx001"
