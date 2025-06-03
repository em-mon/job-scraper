import requests
import string
from bs4 import BeautifulSoup

# Data scraping function
def get_data(url):
    request = requests.get(url)
    return request.text

# Parse to get HTML code
def get_html(url):
    html_data = get_data(url)
    soup = BeautifulSoup(html_data, 'html.parser')
    return soup

# I want: title, company, link, date posted, if i applied or not, requirements

# Get job title
def title_data(soup):
    titles = []
    for products in soup.find_all("a", class_="klavika simpletextlistitem"):
        title = products.get_text(strip=True)
        titles.append(title)
    return titles

def product_data(url):
    title_res = []
    for letter in string.ascii_lowercase:
        base_url = "https://incidecoder.com/search?query="+letter+"&activetab=products"
        page = 1

        while True:
            complete_url = base_url
            if page > 1:
                complete_url = base_url + "&ppage=" + str(page)
            soup = get_html(complete_url)
            title_res += title_data(soup)
            next_page = soup.find("a", string="Next page >>")
            if not next_page:
                break
            page += 1
    return list(set(title_res))

if __name__ == "__main__":
    url = "https://incidecoder.com/products"
    products = product_data(url)
    # temp = 0
    # for i in range(len(products)):
    #     print("Product brand: " + products[i])
