from requests import get
from re import match
from csv import writer
from bs4 import BeautifulSoup
from multiprocess import Pool

URL = 'https://rubilnik.ru/catalog/elektroustanovochnye_izdeliya/elektroustanovochnye_izdeliya_schneider_electric/?PAGEN_1=1'

def write_csv(data):
    with open('products.csv', 'a', encoding='utf-8', newline='') as f:
        csv_writer = writer(f)
        csv_writer.writerow((data['product_name'],
                         data['vendor_code'],
                         data['product_count'],
                         data['product_price']))

def get_html(url):
    r = get(url)
    return r.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    total_pages = soup.find('div', class_='bottom_nav').find_all('a')[-1].text
    return int(total_pages)

def get_product_data(html):
    soup = BeautifulSoup(html, 'lxml')
    product_name = soup.find('h1', id='pagetitle').text.strip()
    vendor_code = soup.find('div', class_='article iblock').find('span', class_='value').text.strip()
    product_count = soup.find('div', class_='item-stock').find('span', class_='value').find('span').text.strip()
    count = match('\((.+)\)', product_count)
    if count:
        product_count = count[1] + ' шт.'
    try:
        product_price = soup.find('div', id='cena_rozn').find('div', class_='cena_celaya_chast').find('span').text.strip() + ' руб.'
    except:
        product_price = soup.find('div', class_='prices_block').find('span', class_='price_value').text.strip() + ' руб.'
    grabbed_data = {'product_name': product_name,
                    'vendor_code': vendor_code,
                    'product_count': product_count,
                    'product_price': product_price}
    write_csv(grabbed_data)

def get_links_from_page(html):
    soup = BeautifulSoup(html, 'lxml')
    products = soup.find('div', class_='catalog_block items block_list').find_all('a', class_='thumb')
    for product in products:
        product_href = 'https://rubilnik.ru' + product.get('href')
        get_product_data(get_html(product_href))

def run_threads(i):
    get_links_from_page(get_html(URL[:-1]+str(i)))
    print(i)

def main():
    total_pages = get_total_pages(get_html(URL)) + 1
    with Pool(40) as p:
        p.map(run_threads, range(1, total_pages))

if __name__ == '__main__':
    main()
