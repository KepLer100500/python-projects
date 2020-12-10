from requests import get, Response
from bs4 import BeautifulSoup
from time import sleep
from random import choice, uniform
from os import makedirs
from os.path import abspath, exists


class Image_saver:
    def __init__(self):
        self.user_agent_list = self.get_user_agents()
        self.raw_proxies = self.get_raw_proxies()
        self.proxies = self.check_proxy(self.raw_proxies, self.user_agent_list)
        self.links = self.get_links(self.user_agent_list, self.proxies)
        self.get_images_links(self.links, self.user_agent_list, self.proxies)

    def get_soup(self, html):
        return BeautifulSoup(html, 'lxml')

    def get_user_agents(self):
        return open('user_agents.txt').read().split('\n')

    def get_raw_proxies(self):
        url = 'https://hidemy.name/ru/proxy-list/?maxtime=1500&ports=80,8080,18080&type=s&anon=4#list'
        proxy_html = get(url, headers={'User-Agent': choice(self.user_agent_list)}).text
        proxy_list = self.get_soup(proxy_html).find('div', class_='table_block').find_all('td')
        return ['https://' + proxy_list[i].text + ':' + proxy_list[i+1].text for i in range(7, len(proxy_list), 7)]

    def check_proxy(self, proxy_list, user_agent_list):
        url = 'https://hidemy.name/ru/what-is-my-ip/'
        good_proxies = list()
        for proxy in proxy_list:
            sleep(uniform(2, 5))
            try:
                proxy_html = get(url,
                                 headers={'User-Agent': choice(self.user_agent_list)},
                                 proxies={'https': proxy}).text
                ip = self.get_soup(proxy_html).find('div', class_='ip').text.strip()
            except:
                ip = False
            if ip:
                good_proxies.append(proxy)
                print('Find good proxy:', proxy)
        return good_proxies

    def get_links(self, user_agent_list, proxies):
        url = 'https://www.mebelstyle.ru/cat/myagkaya-mebel/'
        for proxy in proxies:
            try:
                page = get(url, headers={'User-Agent': choice(user_agent_list)}, proxies={'https': proxy}).text
            except:
                self.proxies.remove(proxy)
        print('Proxy which open target site:', self.proxies)
        links =  self.get_soup(page).find('div', class_='collection-list').find_all('a', class_='collection-item-name')
        links = ['https://www.mebelstyle.ru' + link.get('href') for link in links if link.get('href') != None]
        return links

    def get_images_links(self, links, user_agent_list, proxies):
        for link in links:
            print('Get images from page:', link)
            sleep(uniform(2, 5))
            folder = link.split('/')[-2]
            if not exists(folder):
                makedirs(folder)
            path = abspath(folder)
            page = get(link, headers={'User-Agent': choice(self.user_agent_list)}, proxies={'https': choice(proxies)}).text
            images_from_page = self.get_soup(page).find('div', class_='main-photo').find_all('img', loading='lazy')
            images_from_page = ['https://www.mebelstyle.ru' + image.get('src') for image in images_from_page]
            for image in images_from_page:
                sleep(uniform(1, 2))
                full_name = path + '\\' + image.split('/')[-2] + '_' + image.split('/')[-1]
                file_obj = get(image, stream=True, headers={'User-Agent': choice(self.user_agent_list)}, proxies={'https': choice(proxies)})
                self.save_image(full_name, file_obj)

    def save_image(self, full_name, file_obj):
        with open(full_name, 'bw') as f:
            for chunk in file_obj.iter_content(8192):
                f.write(chunk)


def main():
    image_saver = Image_saver()

if __name__ == '__main__':
    main()
