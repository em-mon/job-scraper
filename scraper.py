import requests
import string
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

def extract_titles(soup):
    return [a.get_text(strip=True) for a in soup.find_all("a", class_="klavika simpletextlistitem")]

def product_data():
    seen = set()
    for letter in string.ascii_lowercase:
        page = 1
        while True:
            url = (
                "https://incidecoder.com/search?query=" +
                letter + "&activetab=products" +
                ("&ppage=" + str(page) if page > 1 else "")
            )
            soup = get_html(url)
            for title in extract_titles(soup):
                seen.add(title)

            next_page = soup.find("a", string="Next page >>")
            if not next_page:
                break
            page += 1
    return list(seen)

if __name__ == "__main__":
    products = product_data()
    print("Total unique products:", len(products))
    # Uncomment below to print all
    # for title in products:
    #     print("Product brand:", title)
    #     print("----source venv/bin/activate
