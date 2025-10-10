import requests

request = requests.get('https://quotes.toscrape.com')
html = request.text
for line in html.split('\n'):
    if '<span class="text" itemprop="text">' in line:
        line = line.replace('<span class="text" itemprop="text">', '')
        line = line.replace('</span>', '')
        quote = line.strip()
        print(quote)
    if '<small class="author" itemprop="author">' in line:
        line = line.replace('<span>by <small class="author" itemprop="author">', '')
        line = line.replace('</small>', '')
        author = line.strip()
        print(author)