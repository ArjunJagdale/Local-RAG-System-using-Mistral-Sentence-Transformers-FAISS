import requests
from bs4 import BeautifulSoup

def scrape_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    texts = [p.get_text() for p in soup.find_all("p")]
    return "\n".join(texts)
