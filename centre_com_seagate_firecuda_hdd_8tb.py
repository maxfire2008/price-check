import bs4
import requests


def price_check():
    # https://www.centrecom.com.au/seagate-firecuda-hdd-8tb-7200rpm-35-internal-hard-drive

    # <div class="prod_price_current product-price">
    #     <span>$319</span>
    # </div>

    page = requests.get(
        "https://www.centrecom.com.au/seagate-firecuda-hdd-8tb-7200rpm-35-internal-hard-drive",
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )
    soup = bs4.BeautifulSoup(page.text, "html.parser")

    # get price as an integer
    price = soup.find(
        "div", {"class": "prod_price_current product-price"}).find("span").text

    print("Firecuda 8TB at Centre Com is now " + price)

    if price != "$325":
        print("Price has changed!")
        return "Price has changed! Firecuda 8TB at Centre Com is now " + \
            price + \
            " https://www.centrecom.com.au/seagate-firecuda-hdd-8tb-7200rpm-35-internal-hard-drive"
