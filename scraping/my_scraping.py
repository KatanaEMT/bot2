from parsel import Selector
import requests


class AnimeScraper:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
    }

    URL = 'https://rezka.ag/animation/adventures/'
    ANIME_XPATH = '//div[@class="b-content__inline_item-cover"]/a/@href'
    ANIME_PLUS_URL = 'https://rezka.ag/animation/'

    def anime_parse_data(self):
        html = requests.get(url=self.URL, headers=self.headers).text
        tree = Selector(text=html)
        links = tree.xpath(self.ANIME_XPATH).extract()
        for link in links:
            print(link)
        return links


if __name__ == "__main__":
    scraper = AnimeScraper()
    scraper.anime_parse_data()