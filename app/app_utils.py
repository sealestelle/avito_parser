from bs4 import BeautifulSoup
from requests import get
from urllib.parse import quote
import base64


def get_count(search: str, area: str) -> int:
    html = get('https://avito.ru/' + area + '?q=' + quote(search)).text
    soup = BeautifulSoup(html, 'lxml')
    count = soup.find('span', attrs={'data-marker': 'page-title/count'})
    return int(count.string.replace(' ', ''))


def get_top(search: str, area: str) -> list:
    html = get('https://avito.ru/' + area + '?q=' + quote(search)).text
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find_all('div', attrs={'data-marker': 'item'})
    top = dict()
    top_list = []
    for i in range(5):
        title = ads[i].find('a', attrs={'data-marker': 'item-title'})['title']
        link = ads[i].find('a', attrs={'data-marker': 'item-title'})['href']
        link = 'https://avito.ru/' + link
        # print(link)
        top['title'] = title
        top['link'] = link
        print(top)
        top_list.append(top.copy())
    return top_list


def decode_from_base64(base64_string: str) -> str:
    base64_bytes = base64_string.encode('UTF-8')
    string_bytes = base64.b64decode(base64_bytes)
    string = string_bytes.decode('UTF-8')
    return string


def encode_to_base64(string: str) -> str:
    string_bytes = string.encode('UTF-8')
    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode('UTF-8')
    return base64_string
