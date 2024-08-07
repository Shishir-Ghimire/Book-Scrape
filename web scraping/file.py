import requests
from bs4 import BeautifulSoup

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

for page in range(1, 51):  # Adjusting the range as necessary
    url = base_url.format(page)
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    book_containers = soup.find_all('article', class_='product_pod')

    for book in book_containers:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').get_text()
        print(f'Title: {title}, Price: {price}')