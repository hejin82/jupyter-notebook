import requests

with open('authors.txt', 'w') as f:
    for i in range(1, 11):
        url = f'https://quotes.toscrape.com/page/{i}'
        request = requests.get(url)
        html = request.text
        for line in html.split('\n'):
            if '<small class="author" itemprop="author">' in line:
                line = line.replace('<span>by <small class="author" itemprop="author">', '')
                line = line.replace('</small>', '')
                author = line.strip()
                f.write(author)
                f.write('\n')