import requests
from bs4 import BeautifulSoup

def scrape_amazon():
    print("Scraping Amazon...")

    headers = {
        "User-Agent": "Mozilla/5.0",
    }

    url = "https://www.amazon.in/s?k=trending+products"
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find_all("div", {"data-component-type": "s-search-result"})

    products = []

    for item in items[:1]:  # Only 1 product 
        title = item.h2.text.strip() if item.h2 else "Unknown Product"
        link = "https://amazon.in" + item.h2.a["href"] if item.h2 else ""
        products.append({
            "title": title,
            "url": link
        })

    if not products:
        print("Amazon returned 0 products. Using fallback sample product.\n")
        products = [{
            "title": "Wireless Bluetooth Earbuds",
            "url": "https://amazon.in"
        }]

    return products
