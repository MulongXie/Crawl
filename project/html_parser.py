from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import re


class Parser:

    def _get_url(self, soup, url):
        new_urls = []
        links = soup.find_all('a', href=re.compile(r'/item'))
        print("related links:", len(links))
        for link in links:
            try:
                new_url = link['href']
                new_url = urljoin(url, new_url)
                new_urls.append(new_url)
            except:
                print('no href')
        return new_urls

    # parse title and summary
    def _get_content(self, soup, url):
        data = {}
        # restore data
        data['url'] = url
        try:
            # further content(title,summary...)
            # <dd class="lemmaWgt-lemmaTitle-title">
            title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
            data['title'] = title.get_text()
            print('title:', title.get_text())

            # <div class="lemma-summary" label-module="lemmaSummary">
            summary = soup.find('div', class_="lemma-summary")
            data['summary'] = summary.get_text()
        except:
            return data
        return data

    def parse(self, pageurl, content):
        if pageurl is None or content is None:
            return
        soup = bs(content, 'html.parser')
        new_urls = self._get_url(soup, pageurl)
        new_data = self._get_content(soup, pageurl)
        return new_urls, new_data

