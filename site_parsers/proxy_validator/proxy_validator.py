from requests import get
from bs4 import BeautifulSoup
from time import sleep
from random import uniform, choice


class Validator():
    def __init__(self, url):
        # init class
        self.url = url
        self.proxies = self.get_proxy()
        self.get_data(url, self.proxies)

    def get_html(self, url, useragent=None, proxy=None):
        # download page
        return get(url, headers=useragent, proxies=proxy).text

    def get_soup(self, html):
        # create object BeautifulSoup type
        return BeautifulSoup(html, 'lxml')

    def print_network_params(self, soup):
        # get ip and User-Agent form hidemy.name
        ip = soup.find('div', class_='ip').text.strip()
        user_agent = soup.find('div', class_='details_browser_data').find_all('td')
        user_agent = user_agent[3].text.strip()
        print(ip, user_agent)

    def get_user_agents(self):
        # generate User-Agent from file
        user_agents = open('user_agents.txt').read().split('\n')
        return {'User-Agent': choice(user_agents)}

    def get_proxy(self):
        # get proxy list from hidemy.name, only https proxies
        proxy_html = self.get_html('https://hidemy.name/ru/proxy-list/?maxtime=1000&type=s&anon=4#list', self.get_user_agents())
        proxies = self.get_soup(proxy_html).find('div', class_='table_block').find_all('td')
        return ['https://' + proxies[i].text + ':' + proxies[i+1].text for i in range(7, len(proxies), 7)]

    def get_data(self, url, proxies):
        # check changing ip on hidemy.name
        for proxy in proxies:
            sleep(uniform(2, 5))
            print(proxy)
            try:
                self.html = self.get_html(url, self.get_user_agents(), {'https': proxy})
                self.soup = self.get_soup(self.html)
                self.print_network_params(self.soup)
            except:
                continue


def main():
    url = 'https://hidemy.name/ru/what-is-my-ip/'
    check = Validator(url)

if __name__ == '__main__':
    main()
