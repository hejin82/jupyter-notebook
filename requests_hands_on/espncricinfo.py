import json
import requests

url = 'https://www.espncricinfo.com/ci/content/story/data/index.json?;type=7;page=1'
headers = {
    "Accept": "application/json",
    "Authorization": "Bearer your_access_token",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}
request = requests.get(url, headers=headers)
data = json.loads(request.text)
for news in data:
    print(news)