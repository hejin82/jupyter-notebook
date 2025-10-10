from bs4 import BeautifulSoup
import requests

json_headers = {
    "Accept": "application/json",
    "Authorization": "Bearer your_access_token",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}
url = f'https://quotes.toscrape.com/'
request = requests.get(url)
soup = BeautifulSoup(request.text, 'html5lib')
with open('bs4quotes.txt', 'w') as f:
    for tag in soup.find_all('span', {'class': 'text'}):
        f.write(tag.string)
        f.write('\n')

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Authorization": "Bearer your_access_token",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}
request = requests.get('https://www.imdb.com/chart/top', headers=headers)
html = request.text
soup = BeautifulSoup(html, 'html5lib')
ul = soup.find('ul', {'class': 'ipc-metadata-list'})
lis = ul.find_all('li')
for li in lis:
    name_link = li.find('a', {'class': 'ipc-title-link-wrapper'})
    name = name_link.find('h3', {'class': 'ipc-title__text'})
    rating = li.find('span', {'class': 'ipc-rating-star--rating'})
    print(rating)
    print(name)




