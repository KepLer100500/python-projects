import requests
import re
import csv
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    tag_pagination_root = re.findall(r'pagination-root-\w+', html)[0]
    pagination_item = re.findall(r'pagination-item-\w+', html)[-1]
    total_pages = soup.find('div', class_=tag_pagination_root).find_all('span', class_=pagination_item)[-2].text
    return int(total_pages)

def write_csv(data):
    with open('avito.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow((data['year'],
                         data['price'],
                         data['params'],
                         data['link']))

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='snippet-list js-catalog_serp').find_all('div' ,class_='item__line')
    for ad in ads:
        try:
            year = ad.find('a', class_='snippet-link').find('span').text.split(',')[1].strip()
        except:
            year = ''
        try:
            link = 'https://www.avito.ru/' + ad.find('a', class_='snippet-link').get('href')
        except:
            link = ''
        try:
            price = ad.find('div', class_='snippet-price-row').find('span').text.strip().replace(' ', '')
        except:
            price = ''
        try:
            params = ad.find('div', class_='specific-params').text.strip().replace('\n', '')
        except:
            params = ''
        data = {'year': year,
                'price': price,
                'params': params,
                'link': link}
        write_csv(data)

def main():
    url = 'https://www.avito.ru/astrahan/avtomobili?radius=200&q=opel+astra&p=1'
    total_pages = get_total_pages(get_html(url))
    for i in range(1, total_pages):
        get_page_data(get_html(url[:-1] + str(i)))

if __name__ == '__main__':
    main()
