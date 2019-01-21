import html_downloader
import html_output
import html_parser
import url_manager


class SpiderMain:

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.Downloader()
        self.parser = html_parser.Parser()
        self.outputer = html_output.Outputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():

            new_url = self.urls.get_new_url()  # 1. fetch new url by url manager
            print('url %d : %s' % (count, new_url))
            content = self.downloader.download(new_url)  # 2. download webpage by downloader
            new_urls, new_data = self.parser.parse(new_url, content)  # 3. parse by parser
            self.urls.add_new_urls(new_urls)
            self.outputer.collect_data(new_data)

            if count == 100:
                break
            count += 1

        self.outputer.output()


if __name__ == '__main__':
    root = 'https://baike.baidu.com/item/Python/407313'
    obj_spider = SpiderMain()
    obj_spider.craw(root)
